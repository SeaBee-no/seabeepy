# Standard python library
import configparser
import sys
import os
import argparse
from collections import namedtuple
import pathlib

# From the gref4hsi library
from gref4hsi.scripts import georeference
from gref4hsi.scripts import orthorectification
from gref4hsi.utils import parsing_utils, specim_parsing_utils
from gref4hsi.utils.config_utils import prepend_data_dir_to_relative_paths, customize_config


import numpy as np
import yaml
"""
This script is meant to be used for the processing pipeline of airborne HI data from the Specim AFX10 instrument.
"""




def main(config_yaml, specim_mission_folder, geoid_path, config_template_path, lab_calibration_path, fast_mode):
    
    # Read flight-specific yaml file
    with open(config_yaml, 'r') as file:  
        config_data = yaml.safe_load(file)
    
    
    # assigning the arguments to variables for simple backwards compatibility
    SPECIM_MISSION_FOLDER = specim_mission_folder
    EPSG_CODE = config_data['mission_epsg']
    RESOLUTION_ORTHOMOSAIC = config_data['resolution_orthomosaic']
    CALIBRATION_DIRECTORY = lab_calibration_path
    
    
    dem_fold = os.path.join(specim_mission_folder, "dem")
    
    
    # Decide whether to use geoid or local terrain model (must be put in /dem folder)
    if not os.path.exists(dem_fold):
        print('DEM folder does not exist so Geoid is used as terrain instead')
        TERRAIN_TYPE = "geoid"
    else:
        if not os.listdir(dem_fold):
            print(f"The folder '{dem_fold}' is empty so Geoid is used as terrain instead.")
            TERRAIN_TYPE = "geoid"
        else:
            # Find the *.tif file using glob
            files = [f for f in os.listdir(directory) if f not in ('.', '..')]
            DEM_PATH = files[0]
            print(f"The file '{dem_path}' is used as terrain.")
            TERRAIN_TYPE = "dem_file"
            
    
    
    GEOID_PATH = geoid_path

    # Settings associated with preprocessing of data from Specim Proprietary data to pipeline-compatible data
    SettingsPreprocess = namedtuple('SettingsPreprocessing', ['dtype_datacube', 
                                                                            'lines_per_chunk', 
                                                                            'specim_raw_mission_dir',
                                                                            'cal_dir',
                                                                            'reformatted_missions_dir',
                                                                            'rotation_matrix_hsi_to_body',
                                                                            'translation_body_to_hsi',
                                                                            'config_file_name'])

    config_specim_preprocess = SettingsPreprocess(dtype_datacube = np.float32, # The data type for the datacube
                                lines_per_chunk= 2000,  # Raw datacube is chunked into this many lines. GB_per_chunk = lines_per_chunk*n_pixels*n_bands*4 bytes
                                specim_raw_mission_dir = SPECIM_MISSION_FOLDER, # Folder containing several mission
                                cal_dir = CALIBRATION_DIRECTORY,  # Calibration directory holding all calibrations at all binning levels
                                reformatted_missions_dir = os.path.join(SPECIM_MISSION_FOLDER, 'processed'), # The fill value for empty cells (select values not occcuring in cube or ancillary data)
                                rotation_matrix_hsi_to_body = np.array([[0, 1, 0],
                                                                        [-1, 0, 0],
                                                                        [0, 0, 1]]), # Rotation matrix R rotating so that vec_body = R*vec_hsi.
                                translation_body_to_hsi = np.array([0, 0, 0]), # Translation t so that vec_body_to_object = vec_hsi_to_object + t
                                # For large files, RAM issues could be a concern. For rectified files exeeding this size, data is written chunk-wize to a memory map.
                                config_file_name = 'configuration.ini')



    # Where to place the config
    DATA_DIR = config_specim_preprocess.reformatted_missions_dir
    config_file_mission = os.path.join(DATA_DIR, 'configuration.ini')


    # Read config from a template (relative path):
    # Set the data directory for the mission, and create empty folder structure
    prepend_data_dir_to_relative_paths(config_path=config_template_path, DATA_DIR=DATA_DIR)

    # Non-default settings
    custom_config = {'General':
                        {'mission_dir': DATA_DIR,
                        'model_export_type': TERRAIN_TYPE, # Ray trace onto geoid or not
                        'max_ray_length': 200}, # Max distance in meters from spectral imager to seafloor. Specim does not fly higher

                    'Coordinate Reference Systems':
                        {'proj_epsg' : EPSG_CODE, # The projected CRS UTM 32, common on mainland norway
                        'geocsc_epsg_export' : 4978, # 3D cartesian system for earth. consistent with GPS frame (but inconsistent with eurasian techtonic plate)
                        'dem_epsg' : EPSG_CODE, # (Optional) If you have a DEM this can be used
                        'pos_epsg_orig' : 4978}, # The CRS of the positioning data we deliver to the georeferencing

                    'Orthorectification':
                        {'resample_rgb_only': False, # True can be good choice for speed during DEV
                        'resolutionhyperspectralmosaic': RESOLUTION_ORTHOMOSAIC, # Resolution in m
                        'raster_transform_method': 'north_east'}, # North-east oriented rasters.
                    
                    'HDF.raw_nav': {
                        'rotation_reference_type' : 'eul_ZYX', # The vehicle orientations are given in Yaw, Pitch, Roll from the NAV system
                        'is_global_rot' : False, # The vehicles orientations from NAV system are Yaw, Pitch, Roll
                        'eul_is_degrees' : True}, # And given in degrees
                    'Absolute Paths': {
                        'geoid_path' : GEOID_PATH,
                        #'geoid_path' : 'data/world/geoids/egm08_25.gtx',
                        # (above) The georeferencing allows processing using norwegian geoid NN2000 and worldwide EGM2008. Also, use of seafloor terrain models are supported. '
                        # At the moment refractive ray tracing is not implemented, but it could be relatively easy by first ray tracing with geoid+tide, 
                        # and then ray tracing from water
                        #'tide_path' : 'D:/HyperspectralDataAll/HI/2022-08-31-060000-Remoy-Specim/Input/tidevann_nn2000_NMA.txt'
                        }
                        # Tide data can be downloaded from https://www.kartverket.no/til-sjos/se-havniva
                        # Preferably it is downloaded with reference "NN2000" to agree with DEM
                    
    }
    
    if fast_mode:
        custom_config['Orthorectification']['resample_rgb_only'] = True
        custom_config['Orthorectification']['resolutionhyperspectralmosaic'] = 1

    if TERRAIN_TYPE == 'geoid':
        custom_config['Absolute Paths']['geoid_path'] = GEOID_PATH
        #'geoid_path' : 'data/world/geoids/egm08_25.gtx'
    elif TERRAIN_TYPE == 'dem_file':
        custom_config['Absolute Paths']['dem_path'] = DEM_PATH

    # Customizes the config file according to settings
    customize_config(config_path=config_file_mission, dict_custom=custom_config)


    config = configparser.ConfigParser()
    config.read(config_file_mission)

    # This function parses raw specim data including (spectral, radiometric, geometric) calibrations and nav data
    # into an h5 file. The nav data is written to "raw/nav/" subfolders, whereas hyperspectral data and calibration data are
    # written to "processed/hyperspectral/" and "processed/calibration/" subfolders.
    # Lastly you need a camera calibration file describing boresight rotations, lever arms focal length and distortion for the pushbroom scanner
    specim_parsing_utils.main(config=config,
                              config_specim=config_specim_preprocess)

    
    # Interpolates and reformats the pose (of the vehicle body) to "processed/nav/" folder.
    config = parsing_utils.export_pose(config_file_mission)
    
    # Exports model
    parsing_utils.export_model(config_file_mission)

    # Georeference the line scans of the hyperspectral imager by ray tracing. Additional or ancillary data about the intersections is automatically computed such as view-angles, sun angles, surface normals as these often affect the measured radiance.
    georeference.main(config_file_mission)
    
    # The data is orthorectified to specified resolution, EPSG projection code (e.g. UTM varieties). Other info is also orthorectified in the process such as time, pixel number, and the various intersection geometries.
    orthorectification.main(config_file_mission)


if __name__ == "__main__":
    main()
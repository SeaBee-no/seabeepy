# Standard python library
import configparser
import sys
import os
import argparse
from collections import namedtuple
import pathlib
import yaml


# Local resources
from gref4hsi.scripts import georeference, orthorectification, coregistration
from gref4hsi.utils import parsing_utils, specim_parsing_utils
from gref4hsi.utils import visualize
from gref4hsi.utils.config_utils import prepend_data_dir_to_relative_paths, customize_config


import numpy as np

"""
This script is meant to be used for testing the processing pipeline of airborne HI data from the Specim AFX10 instrument.
"""

# Make it simple to swap when working a bit on windows and a bit on Linux



def main(config_yaml, specim_mission_folder, geoid_path, config_template_path, lab_calibration_path, fast_mode = False):
    # Read flight-specific yaml file
    with open(config_yaml, 'r') as file:  
        config_data = yaml.safe_load(file)
    
    
    # assigning the arguments to variables for simple backwards compatibility
    SPECIM_MISSION_FOLDER = specim_mission_folder
    EPSG_CODE = config_data['mission_epsg']
    RESOLUTION_ORTHOMOSAIC = config_data['resolution_orthomosaic']
    CALIBRATION_DIRECTORY = lab_calibration_path
    
    
    dem_fold = os.path.join(specim_mission_folder, "dem")

    if not os.path.exists(dem_fold):
        print('DEM folder does not exist so Geoid is used as terrain instead')
        TERRAIN_TYPE = "geoid"
    else:
        if not os.listdir(dem_fold):
            #print(f"The folder '{dem_fold}' is empty so Geoid is used as terrain instead.")
            TERRAIN_TYPE = "geoid"
        else:
            # If there is a folder and it is not empty
            # Find the only file that is there
            files = [f for f in os.listdir(dem_fold) if f not in ('.', '..')]
            DEM_PATH = os.path.join(dem_fold, files[0])
            #print(f"The file '{DEM_PATH}' is used as terrain.")
            TERRAIN_TYPE = "dem_file"
    
    
    # Do coregistration if there is an orthomosaic to compare under "orthomosaic"
    #do_coreg = True
    ortho_ref_fold = os.path.join(specim_mission_folder, "orthomosaic")
    do_coreg = False
    if not os.path.exists(ortho_ref_fold):
        print('Coregistration is not done, as there was no reference orthomosaic')
        
    else:
        if not os.listdir(ortho_ref_fold):
            print('Coregistration is not done, as there was no reference orthomosaic')
        else:
            # If there is a folder and it is not empty
            # Find the only file that is there
            ortho_ref_file = [f for f in os.listdir(ortho_ref_fold) if f not in ('.', '..')][0]
            do_coreg = True
            print(f"The file '{ortho_ref_file}' is used as as reference orthomosaic.")
            
    
    
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
                                lines_per_chunk= 8000,  # Raw datacube is chunked into this many lines. GB_per_chunk = lines_per_chunk*n_pixels*n_bands*4 bytes
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


    # Set the data directory for the mission, and create empty folder structure
    prepend_data_dir_to_relative_paths(config_path=config_template_path, DATA_DIR=DATA_DIR)

    # Non-default settings
    custom_config = {'General':
                        {'mission_dir': DATA_DIR,
                        'model_export_type': TERRAIN_TYPE, # Ray trace onto geoid
                        'max_ray_length': 150}, # Max distance in meters from spectral imager to seafloor. Specim does not fly higher

                    'Coordinate Reference Systems':
                        {'proj_epsg' : EPSG_CODE, # The projected CRS UTM 32, common on mainland norway
                        'geocsc_epsg_export' : 4978, # 3D cartesian system for earth consistent with GPS frame (but inconsistent with eurasian techtonic plate)
                        'dem_epsg' : EPSG_CODE, # (Optional) If you have a DEM this can be used
                        'pos_epsg_orig' : 4978}, # The CRS of the positioning data we deliver to the georeferencing

                    'Orthorectification':
                        {'resample_rgb_only': False, # True can be good choice for speed during DEV
                         'resample_ancillary': True,
                        'resolutionhyperspectralmosaic': RESOLUTION_ORTHOMOSAIC, # Resolution in m
                        'raster_transform_method': 'north_east'}, # North-east oriented rasters.
                    
                    'HDF.raw_nav': {
                        'rotation_reference_type' : 'eul_ZYX', # The vehicle orientations are given in Yaw, Pitch, Roll from the NAV system
                        'is_global_rot' : False, # The vehicles orientations from NAV system are Yaw, Pitch, Roll
                        'eul_is_degrees' : True}, # And given in degrees
                    'Absolute Paths': {
                        'geoid_path' : GEOID_PATH,
                        'orthomosaic_reference_folder' : os.path.join(specim_mission_folder, "orthomosaic"),
                        'ref_ortho_reshaped' : os.path.join(DATA_DIR, "Intermediate", "RefOrthoResampled"),
                        'ref_gcp_path' : os.path.join(DATA_DIR, "Intermediate", "gcp.csv"),
                        'calib_file_coreg' : os.path.join(DATA_DIR, "Output", "HSI_coreg.xml"),
                        # (above) The georeferencing allows processing using norwegian geoid NN2000 and worldwide EGM2008. Also, use of seafloor terrain models are supported. '
                        # At the moment refractive ray tracing is not implemented, but it could be relatively easy by first ray tracing with geoid+tide, 
                        # and then ray tracing from water
                        #'tide_path' : 'D:/HyperspectralDataAll/HI/2022-08-31-060000-Remoy-Specim/Input/tidevann_nn2000_NMA.txt'
                        },
                    
                    # If coregistration is done, then the data must be stored after processing somewhere
                    'HDF.coregistration': {
                            'position_ecef': 'processed/coreg/position_ecef',
                            'quaternion_ecef' : 'processed/coreg/quaternion_ecef'
                        },
                    # These are the ancillary layers to be orthorectified (can select from all entities in "Georeferencing")
                    'Ancillary': {
                            'position_ecef' : 'processed/nav/position_hsi_ecef',
                            'quaternion_ecef' : 'processed/nav/quaternion_hsi_ecef',
                            'points_ecef_crs' : 'processed/georef/points_ecef_crs',
                            #'points_hsi_crs' : 'processed/georef/point_hsi_frame',
                            #'normals_hsi_crs' : 'processed/georef/normals_hsi_frame',
                            'theta_v' : 'processed/georef/theta_v',
                            'theta_s' : 'processed/georef/theta_s',
                            'phi_v' : 'processed/georef/phi_v',
                            'phi_s' : 'processed/georef/phi_s',
                            #'normals_ned_crs' : 'processed/georef/normals_ned_crs',
                            'unix_time_grid' : 'processed/georef/unix_time_grid', # h5 path
                            'pixel_nr_grid': 'processed/georef/pixel_nr_grid', # h5 path
                            #'frame_nr_grid' : 'processed/georef/frame_nr_grid',
                            #'hsi_tide_gridded' : 'processed/georef/hsi_tide_gridded',
                            'hsi_alts_msl' : 'processed/georef/hsi_alts_msl'
                        }
                    
    }

    if TERRAIN_TYPE == 'geoid':
        custom_config['Absolute Paths']['geoid_path'] = GEOID_PATH
        #'geoid_path' : 'data/world/geoids/egm08_25.gtx'
    elif TERRAIN_TYPE == 'dem_file':
        custom_config['Absolute Paths']['dem_path'] = DEM_PATH

    
    
    if do_coreg:
        # No need to orthorectify the data cube initially when coregistration with RGB composites is done
        custom_config['Orthorectification']['resample_rgb_only'] = True
        
        # Here you can set which camera parameters to optimize
        cam_calibrate_dict = {'calibrate_boresight': False,
                          'calibrate_camera': False,
                          'calibrate_lever_arm': False,
                          'calibrate_cx': False,
                          'calibrate_f': False,
                          'calibrate_k1': False,
                          'calibrate_k2': False,
                          'calibrate_k3': False
                          }

        # Here you can set which time-varying errors to estimate
        calibrate_dict_extr = {'calibrate_pos_x': True,
                          'calibrate_pos_y': True,
                          'calibrate_pos_z': True,
                          'calibrate_roll': False,
                          'calibrate_pitch': False,
                          'calibrate_yaw': True}
        
        coreg_dict = {'calibrate_dict': cam_calibrate_dict,
                      'calibrate_per_transect': True, # Whether to calibrate on each transect seperately (True) or to use an entire set of transects for calibration (False)
                      'calibrate_dict_extr': calibrate_dict_extr,
                      'time_node_spacing': 10, #s (set to really large number to yield single node, constant correction)
                      'hard_threshold_m': 10, # m
                      'pos_err_ref_frame': 'ned', # ['ecef' or 'ned'] The ref frame to estimate position errors in
                      'time_interpolation_method': 'linear',
                      'sigma_param' : np.array([2, 2, 5, 0.1, 0.1, 1]) # north [m], east [m], down [m], roll [deg], pitch [deg], yaw [deg] (is different for RTK/PPK!!!!)
                      }
    else:
        # When no coregistration is done, then resample datacube
        custom_config['Orthorectification']['resample_rgb_only'] = False
    
    # 
    if fast_mode:
        custom_config['Orthorectification']['resample_rgb_only'] = True
        custom_config['Orthorectification']['resolutionhyperspectralmosaic'] = 1


    # Customizes the config file according to settings
    customize_config(config_path=config_file_mission, dict_custom=custom_config)


    config = configparser.ConfigParser()
    config.read(config_file_mission)

    # This function parses raw specim data including (spectral, radiometric, geometric) calibrations and nav data
    # into an h5 file. The nav data is written to "raw/nav/" subfolders, whereas hyperspectral data and calibration data 
    # written to "processed/hyperspectral/" and "processed/calibration/" subfolders
    specim_parsing_utils.main(config=config,
                              config_specim=config_specim_preprocess)
    
    # Time interpolates and reformats the pose (of the vehicle body) to "processed/nav/" folder.
    parsing_utils.export_pose(config_file_mission)
    
    # Formats model to triangular mesh and an earth centered earth fixed / geocentric coordinate system
    parsing_utils.export_model(config_file_mission)

    # Commenting out the georeference step is fine if it has been done

    
    ## Visualize the data 3D photo model from RGB images and the time-resolved positions/orientations
    #visualize.show_mesh_camera(config, show_mesh = True, show_pose = True, ref_frame='ENU')

    # Step 1: Direct georeferencing
    georeference.main(config_file_mission)

    # Step 2: Orthorectify the direct georeferenced data (incl metadata)
    orthorectification.main(config_file_mission)
    


    # Step 3 (optional): Coregistration
    # The coregistration compares to the reference (requires a reference orthomosaic) and optimizes geometric parameters which are used to re-georeference.
    if do_coreg:
        # Coregistration requires that Step 1 and 2 were performed and that resample anc = True
        # Match RGB composite to reference, find features and following data, ground control point (gcp) list, for each feature pair:
        # reference point 3D (from reference), position/orientation of vehicle (using resampled time) and pixel coordinate (using resampled pixel coordinate)
        coregistration.main(config_file_mission, mode='compare', is_calibrated = False)

        # The gcp list allows reprojecting reference points and evaluate the reprojection error,
        # which is used to optimize static geometric parameters (e.g. boresight, camera model...) or dynamic geometric parameters (time-varying nav errors).
        # Settings are currently in coregistration script
        coregistration.main(config_file_mission, mode='calibrate', is_calibrated = False, coreg_dict = coreg_dict)

        # Resample full datacube
        custom_config['Orthorectification']['resample_rgb_only'] = False
        customize_config(config_path=config_file_mission, dict_custom=custom_config)

        # Re-georeference with coregistred parameters
        georeference.main(config_file_mission, use_coreg_param=True)
        
        # Coregister this stuff
        orthorectification.main(config_file_mission)

        # Second round of comparison
        coregistration.main(config_file_mission, mode='compare', is_calibrated = True)
        
        # Check bulk
        coregistration.main(config_file_mission, mode='calibrate', is_calibrated = True, coreg_dict = coreg_dict)
    
    




if __name__ == "__main__":
    # DUMMY CODE
    main()
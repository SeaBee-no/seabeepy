# Standard python library
import configparser
import sys
import os
import argparse
from collections import namedtuple
import pathlib
import yaml


from rad4sea.atmos import OceanRad
import pymap3d as pm
import numpy as np
import spectral as sp



import numpy as np

"""
This script is meant to be used for processing radiance into reflectance.
"""


def prepare_data_for_atmcorr(anc_file_path, spectral_file_path):
    
    radiance_spy_object = sp.io.envi.open(spectral_file_path)
    
    
    anc_image_object = sp.io.envi.open(anc_file_path)
    
    anc_band_list = anc_image_object.metadata['band names']
    anc_nodata = float(anc_image_object.metadata['data ignore value'])


    # The pixel number in gridded form can e.g. be plotted
    unix_time_grid = anc_image_object[:,:, anc_band_list.index('unix_time_grid')]
    altitude_grid_msl = anc_image_object[:,:, anc_band_list.index('hsi_alts_msl')]

    # Create a generic mask
    mask_nodata = np.zeros(unix_time_grid.shape, dtype = bool)
    mask_nodata[unix_time_grid != anc_nodata] = True

    # Find the lon-lat-
    x_ecef = anc_image_object[:,:, anc_band_list.index('position_ecef_0')][mask_nodata].mean()
    y_ecef = anc_image_object[:,:, anc_band_list.index('position_ecef_1')][mask_nodata].mean()
    z_ecef = anc_image_object[:,:, anc_band_list.index('position_ecef_2')][mask_nodata].mean()

    lat, lon, _ = pm.ecef2geodetic(x_ecef,y_ecef, z_ecef)

    timestamp_unix = unix_time_grid[mask_nodata].mean()

    altitude_msl = altitude_grid_msl[mask_nodata].mean()
    
    return radiance_spy_object, timestamp_unix, altitude_msl, lon, lat, mask_nodata
    
    
    



def main(anc_folder, cube_list_refl, cube_folder, radiance_multiplier):
    # If conversion from radiance to reflectance is to be done, 
    
    # Step 1: Copy each data cube
    
    for path in cube_list_refl:
        if path.endswith('.hdr'):
            # Name of data cube file (with suffix "_reflectance")
            filename = os.path.basename(path)
            
            # Name of ancillary data cube file
            filename_no_refl = '_'.join(filename.split('_')[0:-1]) + '.hdr'
            
            anc_file_path = os.path.join(anc_folder, filename_no_refl)
            
            spectral_file_path = os.path.join(cube_folder, filename)
            
            # Convenience script to read out nececcary entities from the rectified data.
            radiance_spy_object, timestamp_unix, altitude_msl, lon, lat, mask_nodata = prepare_data_for_atmcorr(anc_file_path, spectral_file_path)
            
            radiance_data = {"radiance_spy_object": radiance_spy_object, 
                 "radiance_multiplier": radiance_multiplier,
                 "timestamp_unix": timestamp_unix,
                 "altitude_msl": altitude_msl,
                 "lon": lon,
                 "lat": lat,
                 "mask_nodata": mask_nodata}
            
            orad = OceanRad.from_radiance(radiance_data)
            
            orad.write_reflectance()
            
            
            



if __name__ == "__main__":
    # DUMMY CODE
    main()
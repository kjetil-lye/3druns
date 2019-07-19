#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 1 09:25 2019

@author: Kjetil Olsen Lye

Computes the mean and var from a file with samples
"""

import netCDF4
import numpy as np
import argparse
import collections
import os
import sys
import re
import glob


if __name__ == '__main__':


    parser = argparse.ArgumentParser(description="""
Converts the file to teh new file format
            """)

    parser.add_argument('--input_file', type=str, required=True,
                        help='Input file')


    parser.add_argument('--output_file', type=str, required=True,
                        help='Output file')


    args = parser.parse_args()


    attributes = {}
    time = 0.0
    with netCDF4.Dataset(args.output_file,'w', format='NETCDF4_CLASSIC') as outf:
        xdim = None
        ydim = None
        zdim = None
        tdim = None


        for filename in glob.glob(args.input_file):

            with netCDF4.Dataset(filename) as f:
                for v in f.variables.keys():
                    if v == 'time':

                        time = f.variables['time'][0]
                        if tdim is None:
                            tdim = outf.createDimension('t', 1)
                            t = outf.createVariable("time", np.float64, ("t",))
                            t[0] = time
                    else:
                        d = f.variables[v]
                        if xdim is None:
                            xdim = outf.createDimension("x", d.shape[0])
                            ydim = outf.createDimension("y", d.shape[1])
                            zdim = outf.createDimension("z", d.shape[2])

                        newvar = outf.createVariable(variable, d.dtype, ("x", "y", "z"))
                        newvar[:,:,:] = d[:,:,:]

                for attribute_name in f.ncattrs():
                    outf.setncattr(f'sample_{sample}_{attribute_name}',
                        f.getncattr(attribute_name))


                outf.setncattr("WORKING_DIR", os.getcwd())
                outf.setncattr("IMPORTANT_NOTE", """
        This file was converted with the script tools/combine_to_one_file.py
        in the 3druns repository. This was done as a postprocessing step
                    """)


                outf.setncattr("COMMAND_RUN_TO_COMBINE", " ".join([
                            sys.executable,
                            *sys.argv]))

                with open(sys.argv[0]) as scriptfile:
                    outf.setncattr("SCRIPTFILE", scriptfile.read())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 17:48:40 2019

@author: Kjetil Olsen Lye

Converts the netcdf to a single precision file. It also throws away auxillary variables
(p, ux, uy, uz)
"""

import netCDF4
import numpy as np
import argparse

def is_not_auxillary(v):
    for k in ['p', 'ux', 'uy', 'uz']:
        if f"_{k}_" in v:
            return False
    return True

if __name__ == '__main__':
    
    
    parser = argparse.ArgumentParser(description="""
Converts the file to teh new file format
            """)

    parser.add_argument('--input_file', type=str, required=True,
                        help='Input file')

    parser.add_argument('--output_file', type=str, required=True,
                        help='Output file')

    args = parser.parse_args()
    
    xdim = None
    ydim = None
    zdim = None
    with netCDF4.Dataset(args.input_file) as f:
        with netCDF4.Dataset(args.output_file, 'w', format='NETCDF4_CLASSIC') as outf:
            for v in f.variables.keys():
                print(v)
                if v == 'time':
                    tdim = outf.createDimension("t", 1)
                    t = outf.createVariable("time", np.float64, ("t",))
                    t[0] = f.variables[v][0]
                elif is_not_auxillary(v):
                    d = f.variables[v][:,:,:]
                    if xdim is None:
                        xdim = outf.createDimension("x", d.shape[0])
                        ydim = outf.createDimension("y", d.shape[1])
                        zdim = outf.createDimension("z", d.shape[2])
                        
                    newvar = outf.createVariable(v, np.float32, ("x", "y", "z"))
                    newvar[:,:,:] = d[:,:,:].astype(np.float32)
                    
            for attribute_name in f.ncattrs():
                outf.setncattr(attribute_name, f.getncattr(attribute_name))
                        
            outf.setncattr("IMPORTANT_NODE", """
This file was converted with the script tools/convert_to_new_format.py
in the 3druns repository. This was done to save space. It should be a raw copy of the original file, 
except for two details: We now store single precision, and we remove aux variables (p, ux, uy, uz)
            """)
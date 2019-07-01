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

class MeanVarianceComputer:

    def __init__(self):
        self.count = 0
        self.mean = None
        self.m2 = None
        
    def update(self, data):
        if self.mean is None:
            self.mean = np.zeros_like(data, dtype=np.float64)
            self.m2 = np.zeros_like(data, dtype=np.float64)
            
        self.count += 1
        delta = data - self.mean
        self.mean += delta / self.count
        
        delta2 = data - self.mean
        self.m2 += delta * delta2
        
    def get_mean(self):
        return self.mean
    
    def get_variance(self):
        return self.m2/self.count
    
    def __getitem__(self, stat):
        
        if stat == 'mean':
            return self.get_mean()
        elif stat == 'variance':
            return self.get_variance()
        
        raise Exception(f'Unknown statistics: {stat}')
            
if __name__ == '__main__':
    
    
    parser = argparse.ArgumentParser(description="""
Converts the file to teh new file format
            """)

    parser.add_argument('--input_file', type=str, required=True,
                        help='Input file')

    parser.add_argument('--output_file_base', type=str, required=True,
                        help='Output file')


    args = parser.parse_args()
    
   
    time_match = re.search(r'_(\d+).nc', args.input_file)
    if time_match:
        timestep = int(time_match.group(1))
    else:
        timestep = 0
    mean_variance = collections.defaultdict(lambda : MeanVarianceComputer())
    
    attributes = {}
    time = 0.0
    with netCDF4.Dataset(args.input_file) as f:
        
        for v in f.variables.keys():
            if v == 'time':
                time = f.variables['time'][0]
            else:
                d = f.variables[v][:,:,:]
                
                variable_match = re.match(r'sample_(\d+)_(.+)', v)
                variable = str(variable_match.group(2))
                mean_variance[variable].update(d)
             
        for attribute_name in f.ncattrs():
            attributes[attribute_name] = f.getncattr(attribute_name)
            
    for stat in ['mean', 'variance']:
        outname = f'{args.output_file_base}_{stat}_{timestep}.nc'
        with netCDF4.Dataset(outname, 'w', format='NETCDF4_CLASSIC') as outf:
            xdim = None
            ydim = None
            zdim = None

            tdim = outf.createDimension('t', 1)
            t = outf.createVariable("time", np.float64, ("t",))
            t[0] = time
            for variable in mean_variance.keys():
                d = mean_variance[variable][stat]
                if xdim is None:
                    xdim = outf.createDimension("x", d.shape[0])
                    ydim = outf.createDimension("y", d.shape[1])
                    zdim = outf.createDimension("z", d.shape[2])
                    
                newvar = outf.createVariable(variable, d.dtype, ("x", "y", "z"))
                newvar[:,:,:] = d[:,:,:]
           
                        
            outf.setncattr("IMPORTANT_NODE", """
This file was converted with the script tools/compute_mean_var.py
in the 3druns repository. This was done as a postprocessing step
            """)
            
            
            outf.setncattr("COMMAND_RUN_TO_COMPUTE_MEAN_VAR", " ".join([
                    sys.executable,
                    *sys.argv]))
    
            with open(sys.argv[0]) as scriptfile:
                outf.setncattr("SCRIPTFILE", scriptfile.read())
                
            for attr_name, attr_value in attributes.items():
                outf.setncattr(attr_name, attr_value)
                
            

    if args.input_file == args.output_file:
        os.rename(output_file, args.output_file)

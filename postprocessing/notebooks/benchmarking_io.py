"""
Small script to find the optimal way to access
the netcdf files
"""

import netCDF4
import numpy as np
import time
import sys
import collections
import os
import json

def load(i, fname, plane):
    number_of_samples=256
    resolution=256
    variables=['rho', 'mx', 'my', 'mz', 'E']
    with netCDF4.Dataset(fname) as f:
        samples = np.zeros((number_of_samples, resolution, resolution, len(variables)))
        for variable_index, variable in enumerate(variables):
            for sample in range(number_of_samples):
                key = f'sample_{sample}_{variable}'
                if i == 0:
                    samples[sample,:,:,variable_index] = f.variables[key][plane,:,:]
                elif i == 1:
                    samples[sample,:,:,variable_index] = f.variables[key][:,plane,:]
                else:
                    samples[sample,:,:,variable_index] = f.variables[key][:,:,plane]

    return samples

def write_data(times):
    timedict = {}
    for i, time_array in times.items():
        timedict[i] = {}
        for function in [np.mean, np.std, np.min, np.max]:
            timedict[i][function.__name__] = function(time_array)
    
    with open(f'{sys.argv[0]}_{sys.argv[1].replace("/","").replace(" ", "_")}.timings.json', 'w') as f:
        json.dump(timedict, f)
fname=sys.argv[1]

times = collections.defaultdict(list)
resolution=256

for plane in range(resolution):
    for i in range(3):
        print(f"i = {i}, plane = {plane}")
        start_time = time.time()
        load(i, fname, plane)
        end_time = time.time()
        times[i].append(end_time - start_time)
        write_data(times)

for i, time_array in times.items():
    print("#"*80)
    print(f'{i}')
    print(f'mean: {np.mean(time_array)} s')
    print(f'std : {np.std(time_array)} s')
    print(f'min : {np.min(time_array)} s')
    print(f'max : {np.max(time_array)} s')
                

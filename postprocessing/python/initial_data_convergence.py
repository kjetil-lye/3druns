#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 14:07:46 2019

@author: Kjetil Olsen Lye

This script is for debugging initial data. It simply checks that the initial 
data converges.
"""

import sys
import argparse
import numpy as np
import plot_info
import collections
import matplotlib.pyplot as plt

class RandomGenerator:
    def __init__(self, module, varname, size):
        self.module = module
        self.varname = varname
        self.size = size
        
        
    def __call__(self):
        setattr(self.module, self.varname, np.random.uniform(0, 1, self.size))

def plot_convergence(title, init_global, random_generator, samples=128):
    resolutions = [64, 128, 256, 512]
    
    variables = ["rho", "ux", "uy", "uz", "p"]
    
    errors = collections.defaultdict(lambda: np.zeros(len(resolutions)))
    
    
    for n, resolution in enumerate(resolutions):
        print()
        print(f"resolution: {resolution}")
        data_local = collections.defaultdict(lambda : np.zeros((resolution, resolution, resolution)))
        data_coarse = collections.defaultdict(lambda : np.zeros((resolution//2, resolution//2, resolution//2)))
        
        
        for sample in range(samples):
            sys.stdout.write(f'Sample: {sample}\r')
            sys.stdout.flush()
            random_generator()
            init_global(data_local['rho'], 
                        data_local['ux'], 
                        data_local['uz'],
                        data_local['uz'],
                        data_local['p'],
                        resolution, resolution, resolution,
                        0, 0, 0,
                        1, 1, 1)
            
            init_global(data_coarse['rho'], 
                        data_coarse['ux'], 
                        data_coarse['uz'],
                        data_coarse['uz'],
                        data_coarse['p'],
                        resolution//2, resolution//2, resolution//2,
                        0, 0, 0,
                        1, 1, 1)
            
            
            for variable in data_local.keys():
                upscaled_coarse = np.repeat(np.repeat(np.repeat(data_coarse[variable], 2, 0), 2, 1), 2, 2)
                errors[variable][n] += np.sum(abs(data_local[variable]-upscaled_coarse))/resolution**3
            
        errors[variable][n] /= samples
        
    for variable in variables:
        plt.loglog(resolutions, errors[variable], '-o', basex=2, basey=2)
        plt.xticks(resolutions, [f'${r}^3$' for r in resolutions])
        
        plt.xlabel('Resolution ($N^3$)')
        plt.ylabel('Error ($\\mathbb{E}(||u^N-u^{N/2}||)$)')
        plt.title(f'{title}\nVariable: {variable}, samples: {samples}')
        plot_info.savePlot(f'initial_data_convergence_{title}_{variable}')
                

if __name__ == '__main__':
    
    import argparse

    parser = argparse.ArgumentParser(description="""
Computes the wasserstein distances
        """)

    parser.add_argument('--script_file', type=str, required=True,
                        help='Input script file')

    parser.add_argument('--title', type=str, required=True,
                        help='Title of plot')

    parser.add_argument('--aux_parameter_name', type=str, default='epsilon',
                        help='Name of aux parameter')
    
    parser.add_argument('--aux_parameter_value', type=float, default=0.05,
                        help='Value of aux parameter')
    
    parser.add_argument('--random_variable_name', type=str, default='a',
                        help='Name of random variable')
    
    parser.add_argument('--random_variable_size', type=int, default=40,
                        help='Lenght of random parameter')


    args = parser.parse_args()
    
    
    
    import importlib.util
    spec = importlib.util.spec_from_file_location("initaldata", args.script_file)
    initialdata = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(initialdata)
    
    setattr(initialdata, args.aux_parameter_name, args.aux_parameter_value)
    
    for attr, value in np.__dict__.items():
        if not attr.startswith('_'):
            setattr(initialdata, attr, value)
    
    plot_convergence(args.title,
                     initialdata.init_global,
                     RandomGenerator(initialdata, args.random_variable_name, args.random_variable_size))
    
    
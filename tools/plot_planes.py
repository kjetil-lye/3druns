import netCDF4

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import numpy as np
import sys
import os
import plot_info
import argparse

import glob
from xml_tools import set_in_xml, get_xml_node, get_in_xml, read_config

def get_parameters(folder):
    parameters = {}
    for xml_file in glob.glob(os.path.join(folder, "*.xml")):
        if 'report' in xml_file:
            continue
        try:
            config = read_config(xml_file)


            initial_data_parameters = get_xml_node(config, "config.fvm.initialData.parameters")

            for initial_data_parameter in initial_data_parameters.getElementsByTagName("parameter"):
                name = get_in_xml(initial_data_parameter, "name")
                length = int(get_in_xml(initial_data_parameter, "length"))
        
                if length == 1:
                    value = float(get_in_xml(initial_data_parameter, "value"))
                    parameters[name] = value
                    print(parameters)
        except Exception as e:
            print(e)
    return parameters



if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="""
Plot the NetCDF file
        """)

    parser.add_argument('--input_file', type=str, required=True,
                         help='Path to input file')

    parser.add_argument('--sample', type=int, default=0,
                        help="Sample number to plot")

    parser.add_argument('--in_same_dir', action='store_true',
                        help='Output the plot in same directory as the data file')

    parser.add_argument('--variable', type=str, default='rho',
                        help="variable to plot (rho, mx, my, mz, E, p, ux, uy, uz)")




    args = parser.parse_args()
    inname = args.input_file
    sample = args.sample
    variable = args.variable
    
    if "mean" in inname or "variance" in inname:
        sample_key = variable
        if "mean" in inname:
            description = "mean"
        else:
            description = "variance"
    else:
        sample_key = 'sample_{}_{}'.format(sample, variable)
        description = f"sample = ${sample}$"
    M = 4
    fig, axes = plt.subplots(M, 3, sharex='all', sharey='all', figsize=(32,32))
    
    with netCDF4.Dataset(inname) as f:
        if os.path.dirname(inname).strip() != "":
            os.chdir(os.path.dirname(inname))
        parameters = get_parameters(".")
        N = f.variables[sample_key].shape[0]
        title_parameters = ", ".join([f"{key} = ${parameters[key]}$" for key in parameters.keys()])
        fig.suptitle(f'{inname}, grid_size=${N}^3$, {description}, variable={variable}\n{title_parameters}',
                     fontsize=30)
        x, y = np.mgrid[0:1:N*1j, 0:1:N*1j]

        for j in range(0, M):
            ax = axes[j,0]
            d = f.variables[sample_key][:,:,(j*N)//M]

            im = ax.pcolormesh(x, y, d)
            try:
                 ax.set_xlabel('$x$')
                 ax.set_ylabel('$y$')
            except:
                 pass
            fig.colorbar(im, ax=ax)
            ax.set_title("Fixing $z={}$".format(j/M), fontsize=20)
                 
            ax = axes[j, 1]
            d = f.variables[sample_key][:,(j*N)//M,:]

            im = ax.pcolormesh(x, y, d)
            try:
                 ax.set_xlabel('$x$')
                 ax.set_ylabel('$z$')
            except:
                 pass
            fig.colorbar(im, ax=ax)
            ax.set_title("Fixing $y={}$".format(j/M), fontsize=20)

            ax = axes[j, 2]
            d = f.variables[sample_key][(j*N)//M, :, :]

            img = ax.pcolormesh(x, y, d)
            try:
                 ax.set_xlabel('$y$')
                 ax.set_ylabel('$z$')
            except:
                 pass
            fig.colorbar(im, ax=ax)
            ax.set_title("Fixing $x={}$".format(j/M), fontsize=20)
        parameters_as_str = "_".join([f"{key}_{parameters[key]}" for key in parameters.keys()])

        plot_info.savePlot(os.path.splitext(os.path.basename(inname))[0] + "_" + \
                           sample_key + "_resolution_" + str(N) + parameters_as_str)

import netCDF4

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import numpy as np
import sys
import os
import plot_info
import argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="""
Plot the NetCDF file
        """)

    parser.add_argument('--input_file', type=str, required=True,
                         help='Path to input file')

    parser.add_argument('--sample', type=int, default=0,
                        help="Sample number to plot")

    parser.add_argument('--variable', type=str, default='rho',
                        help="variable to plot (rho, mx, my, mz, E, p, ux, uy, uz)")




    args = parser.parse_args()
    inname = args.input_file
    sample = args.sample
    variable = args.variable

    sample_key = 'sample_{}_{}'.format(sample, variable)
    M = 4
    fig, axes = plt.subplots(M, 3, sharex='all', sharey='all', figsize=(32,32))

    with netCDF4.Dataset(inname) as f:
         
        N = f.variables[sample_key].shape[0]
        fig.suptitle('{}, grid_size=${}^3$, sample=${}$, variable={}'.format(inname, \
                                                                            N, \
                                                                            sample,
                                                                            variable),
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
                 ax.set_ylabel('$y$')
            except:
                 pass
                 fig.colorbar(im, ax=ax)
                 ax.set_title("Fixing $y={}$".format(j/M), fontsize=20)

            ax = axes[j, 2]
            d = f.variables[sample_key][(j*N)//M, :, :]

            img = ax.pcolormesh(x, y, d)
            try:
                 ax.set_xlabel('$x$')
                 ax.set_ylabel('$y$')
            except:
                 pass
                 fig.colorbar(im, ax=ax)
                 ax.set_title("Fixing $x={}$".format(j/M), fontsize=20)

        plot_info.savePlot(os.path.splitext(os.path.basename(inname))[0] + "_" + sample_key)

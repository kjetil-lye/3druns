"""
This is used to make a comparison between two runs (eg. differening computational method,
or varying float or double)
"""

import numpy as np
import os
import netCDF4
import latex_plots
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['savefig.dpi'] = 600
import matplotlib.pyplot as plt

import sys
sys.path.append('../python')
import plot_info

latex_stat = {
    'mean' : '\\mathbb{E}',
    'variance' : '\\mathrm{Var}'
    }

latex_variables = {
    'rho' : '\\rho',
    'E'   : 'E',
    'mx' : 'm_x',
    'my' : 'm_y',
    'mz' : 'm_z',
    'ux' : 'u_x',
    'uy' : 'u_y',
    'uz' : 'u_z',
    'p'  : 'p'
}

def resolution_exists(basename, resolution, stat):
    print(basename.format(resolution=resolution, stat=stat))
    if not os.path.exists(basename.format(resolution=resolution,stat=stat)):
        return False

    try:
        load_plane(basename.format(resolution=resolution,stat=stat), 0, 'rho')
    except Exception as e:
        return False

    return True


def load_plane(filename, plane, variable):
    with netCDF4.Dataset(filename) as f:
        for attr in f.ncattrs():
            plot_info.add_additional_plot_parameters(filename.replace("/", "_") + "_" + attr, f.getncattr(attr))
        return f.variables[f'{variable}'][plane,:,:]

def plot_convergence(basename_a, 
                     name_a, 
                     basename_b, 
                     name_b,
                     title, 
                     variable,
                     starting_resolution, 
                     stat,
                     zoom,
                     compute_rate):
    
    resolution = starting_resolution

    resolutions = []
    errors = []
    
    while resolution_exists(basename_a, resolution,stat) and resolution_exists(basename_b, resolution,stat):
        print(resolution)
        error = 0.0
        for plane in range(resolution):
            data_a = load_plane(basename_a.format(resolution=resolution, stat=stat), plane, variable)
            data_b = load_plane(basename_b.format(resolution=resolution, stat=stat), plane, variable)

            error += np.sum(abs(data_a-data_b))
        error /= resolution**3

        errors.append(error)
        resolutions.append(resolution)

        resolution *= 2

    resolutions = np.array(resolutions)

    min_error = np.min(errors)
    max_error = np.max(errors)
    if zoom:
        plt.ylim([2**np.floor(np.log2(min_error)-1), 2**np.ceil(np.log2(max_error)+1)])
    p = plt.loglog(resolutions, errors, '-o', basex=2, basey=2)
    if compute_rate:
        poly = np.polyfit(np.log(resolutions), np.log(errors), 1)
        plt.loglog(resolutions, np.exp(poly[1])*resolutions**poly[0], '--',
                   color=p[0].get_color(),
                   label=f'$\\mathcal{{O}}(N^{{{poly[0]:.2f}}})$',
                   basex=2,
                   basey=2)
        plt.legend()

    plt.xlabel('Resolution ($N^3$)')
    if "_" not in latex_variables[variable]:
        plt.ylabel(f'Error ($\\lVert {latex_stat[stat]}({latex_variables[variable]}^{{N}}_{{\\mathrm{{{name_a}}}}})-{latex_stat[stat]}({latex_variables[variable]}^{{N}}_{{\\mathrm{{{name_b}}}}})\\rVert_{{L^1(D)}}$)')
    else:
        latex_variable_with_subscript_a = f"{latex_variables[variable][:-2]}_{{{latex_variables[variable][-1]}, \\mathrm{{{name_a}}}}}"
        latex_variable_with_subscript_b = f"{latex_variables[variable][:-2]}_{{{latex_variables[variable][-1]}, \\mathrm{{{name_b}}}}}"
        plt.ylabel(f'Error ($\\lVert {latex_stat[stat]}({latex_variable_with_subscript_a}^{{N}})-{latex_stat[stat]}({latex_variable_with_subscript_b}^{{N}})\\rVert_{{L^1(D)}}$)')
    plt.xticks(resolutions, [f"${r}^3$" for r in resolutions])
    plt.title(f"Convergence of {stat},\n"
              f"Comparing {name_a} and {name_b}\n"
              f"{title}\n"
              f"Variable: ${latex_variables[variable]}$")

    plot_info.saveData(f'{stat}_convergence_comparison_{name_a}_{name_b}_{title}_{variable}_errors', errors)
    plot_info.saveData(f'{stat}_convergence_comparison_{name_a}_{name_b}_{title}_{variable}_resolutions', resolutions)

    plot_info.savePlot(f'{stat}_convergence_comparison_{name_a}_{name_b}_{title}_{variable}')

if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser(description="""
Computes the stat convergence comparing two methods.
            """)

    parser.add_argument('--input_basename_a', type=str, required=True,     
                        help='Input filename first (should have a format string {resolution})')
    
    parser.add_argument('--input_basename_b', type=str, required=True,     
                        help='Input filename first (should have a format string {resolution})')
    
    parser.add_argument('--name_b', type=str, required=True,     
                        help='Short descriptive name of basename_b (eg. "float")')
    
    parser.add_argument('--name_a', type=str, required=True,     
                        help='Short descriptive name of basename_a (eg. "double")')

    parser.add_argument('--title', type=str, required=True,
                        help='Title of plot')

    parser.add_argument('--variable', type=str, default='rho',
                        help='Variable')

    parser.add_argument('--starting_resolution', type=int, default=256,
                        help='Starting resolution (smallest resolution)')

    parser.add_argument('--stat', type=str, default='mean',
                        help='Statistics (ether mean or variance)')
    
    parser.add_argument('--not_zoom', action='store_true',
                        help='Disable zooming out of plot. We typically zoom out of plots because matplotlib zooms in so much it seems like it is converging. For fBm with low H, it is usually a good idea to disable this so that we actually see the slow convergence')

    parser.add_argument('--compute_rate', action='store_true',
                        help='Compute the convergence rate')

    
    args = parser.parse_args()


    plot_info.add_additional_plot_parameters("basename_a", args.input_basename_a)
    plot_info.add_additional_plot_parameters("basename_b", args.input_basename_b)

    plot_convergence(args.input_basename_a, 
                     args.name_a,
                     args.input_basename_b, 
                     args.name_b,
                     args.title, args.variable, args.starting_resolution, 
                     args.stat, not args.not_zoom, args.compute_rate)

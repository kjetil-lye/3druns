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
    'p'  : 'p',
    'all': 'u'
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

def plot_convergence(basename, title, variable, starting_resolution, stat, zoom, compute_rate, reference_solution=False):

    if variable != 'all':
        variables = [variable]
    else:
        variables = ['rho', 'mx', 'my', 'mz', 'E']

    resolution = starting_resolution

    resolutions = []
    errors = []
    if reference_solution:
        max_resolution = starting_resolution
        while resolution_exists(basename, max_resolution, stat):
            resolutions.append(max_resolution)
            max_resolution = 2*max_resolution
        print(f'max_resolution = {resolutions[-1]}')
        for resolution in resolutions[:-1]:
            print(resolution)
            error = 0.0
            for plane in range(resolutions[-1]):
                for variable_local in variables:
                    data_fine = load_plane(basename.format(resolution=resolutions[-1], stat=stat), plane, variable_local)
                
                    factor_plane = resolutions[-1]//resolution
                    data_coarse = load_plane(basename.format(resolution=resolution, stat=stat), plane//factor_plane, variable_local)
                
                    while data_coarse.shape[0] < data_fine.shape[0]:
                        data_coarse = np.repeat(np.repeat(data_coarse, 2, 0), 2, 1)

                    error += np.sum(abs(data_coarse-data_fine))
            error /= (resolutions[-1])**3

            errors.append(error)
        resolutions = np.array(resolutions)[:-1]
    else:
        while resolution_exists(basename, resolution,stat) and resolution_exists(basename, 2*resolution,stat):
            print(resolution)
            error = 0.0
            for plane in range(2*resolution):
                for variable_local in variables:
                    data_fine = load_plane(basename.format(resolution=2*resolution, stat=stat), plane, variable_local)
                    data_coarse = np.repeat(np.repeat(load_plane(basename.format(resolution=resolution, stat=stat), plane//2, variable_local), 2, 0), 2, 1)

                    error += np.sum(abs(data_coarse-data_fine))
            error /= (2*resolution)**3

            errors.append(error)
            resolutions.append(resolution)

            resolution *= 2

    
        resolutions = 2*np.array(resolutions)

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
    if reference_solution:
        plt.ylabel(f'Error ($\\lVert {latex_stat[stat]}({latex_variables[variable]}^{{N}})-{latex_stat[stat]}({latex_variables[variable]}^{{{2*resolutions[-1]}}})\\rVert_{{L^1(D)}}$)')
    else:
        plt.ylabel(f'Error ($\\lVert {latex_stat[stat]}({latex_variables[variable]}^{{N}})-{latex_stat[stat]}({latex_variables[variable]}^{{N/2}})\\rVert_{{L^1(D)}}$)')
    plt.xticks(resolutions, [f"${r}^3$" for r in resolutions])
    plt.title(f"Convergence of {stat},\n"
              f"{title}\n"
              f"Variable: ${latex_variables[variable]}$")
    if reference_solution:
        plot_info.saveData(f'{stat}_convergence_reference_{title}_{variable}_errors', errors)
        plot_info.saveData(f'{stat}_convergence_reference_{title}_{variable}_resolutions', resolutions)

        plot_info.savePlot(f'{stat}_convergence_reference_{title}_{variable}')
    else:
        plot_info.saveData(f'{stat}_convergence_{title}_{variable}_errors', errors)
        plot_info.saveData(f'{stat}_convergence_{title}_{variable}_resolutions', resolutions)

        plot_info.savePlot(f'{stat}_convergence_{title}_{variable}')


if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser(description="""
Computes the stat convergence
            """)

    parser.add_argument('--input_basename', type=str, required=True,     
                        help='Input filename (should have a format string {resolution})')

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


    parser.add_argument('--reference_solution', action='store_true',
                        help='Compute convergence against a reference solution')
    
    args = parser.parse_args()


    plot_info.add_additional_plot_parameters("basename", args.input_basename)

    plot_convergence(args.input_basename, args.title, args.variable, args.starting_resolution, args.stat, not args.not_zoom, args.compute_rate, reference_solution=args.reference_solution)

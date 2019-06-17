import numpy as np
import os
import netCDF4
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
            plot_info.add_additional_plot_parameters(attr, f.getncattr(attr))
        return f.variables[f'{variable}'][plane,:,:]

def plot_convergence(basename, title, variable, starting_resolution, stat):
    resolution = starting_resolution

    resolutions = []
    errors = []
    
    while resolution_exists(basename, resolution,stat) and resolution_exists(basename, 2*resolution,stat):
        print(resolution)
        error = 0.0
        for plane in range(2*resolution):
            data_fine = load_plane(basename.format(resolution=2*resolution, stat=stat), plane, variable)
            data_coarse = np.repeat(np.repeat(load_plane(basename.format(resolution=resolution, stat=stat), plane//2, variable), 2, 0), 2, 1)

            error += np.sum(abs(data_coarse-data_fine))
        error /= resolution**3

        errors.append(error)
        resolutions.append(resolution)

        resolution *= 2

    resolutions = 2*np.array(resolutions)

    min_error = np.min(errors)
    max_error = np.max(errors)
    plt.ylim([2**np.floor(np.log2(min_error)-1), 2**np.ceil(np.log2(max_error)+1)])
    plt.loglog(resolutions, errors, '-o', basex=2, basey=2)
    plt.xlabel('Resolution ($N^3$)')
    plt.ylabel(f'Error ($||{latex_stat[stat]}({latex_variables[variable]}^{{N}})-{latex_stat[stat]}({latex_variables[variable]}^{{N/2}})||_{{L^1(D)}}$)')
    plt.xticks(resolutions, [f"${r}^3$" for r in resolutions])
    plt.title(f"Convergence of {stat},\n"
              f"{title}\n"
              f"Variable: ${latex_variables[variable]}$")

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


    
    args = parser.parse_args()


    plot_info.add_additional_plot_parameters("basename", args.input_basename)

    plot_convergence(args.input_basename, args.title, args.variable, args.starting_resolution, args.stat)

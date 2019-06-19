import numpy as np
import os
import netCDF4
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['savefig.dpi'] = 600
# see https://stackoverflow.com/a/46262952 (for norm symbol)
# and https://stackoverflow.com/a/23856968
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}'] #for \text command
import matplotlib.pyplot as plt
import sys
sys.path.append('../python')
import plot_info

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

def resolution_exists(basename, resolution):
    print(basename.format(resolution=resolution))
    if not os.path.exists(basename.format(resolution=resolution)):
        return False

    try:
        load_plane(basename.format(resolution=resolution), 0, 'rho')
    except Exception as e:
        return False

    return True


def load_plane(filename, plane, variable):
    with netCDF4.Dataset(filename) as f:
        for attr in f.ncattrs():
            plot_info.add_additional_plot_parameters(attr, f.getncattr(attr))
        return f.variables[f'sample_0_{variable}'][plane,:,:]

def plot_convergence_single_sample(basename, title, variable, starting_resolution, zoom=True, compute_rate=False):
    resolution = starting_resolution

    resolutions = []
    errors = []
    
    while resolution_exists(basename, resolution) and resolution_exists(basename, 2*resolution):
        print(resolution)
        error = 0.0
        for plane in range(2*resolution):
            data_fine = load_plane(basename.format(resolution=2*resolution), plane, variable)
            data_coarse = np.repeat(np.repeat(load_plane(basename.format(resolution=resolution), plane//2, variable), 2, 0), 2, 1)

            error += np.sum(abs(data_coarse-data_fine))
        error /= resolution**3

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
    plt.ylabel(f'Error ($\\lVert {latex_variables[variable]}^{{N}}-{latex_variables[variable]}^{{N/2}}\\rVert_{{L^1(D)}}$)')
    plt.xticks(resolutions, [f"${r}^3$" for r in resolutions])
    plt.title(f"Convergence of single sample,\n"
              f"{title}\n"
              f"Variable: ${latex_variables[variable]}$")

    plot_info.saveData(f'single_sample_convergence_{title}_{variable}_errors', errors)
    plot_info.saveData(f'single_sample_convergence_{title}_{variable}_resolutions', resolutions)

    plot_info.savePlot(f'single_sample_convergence_{title}_{variable}')

if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser(description="""
Computes the single sample convergence
            """)

    parser.add_argument('--input_basename', type=str, required=True,
                        help='Input filename (should have a format string {resolution})')

    parser.add_argument('--title', type=str, required=True,
                        help='Title of plot')

    parser.add_argument('--not_zoom', action='store_true',
                        help='Disable zooming out of plot. We typically zoom out of plots because matplotlib zooms in so much it seems like it is converging. For fBm with low H, it is usually a good idea to disable this so that we actually see the slow convergence')

    parser.add_argument('--compute_rate', action='store_true',
                        help='Compute the convergence rate')


    parser.add_argument('--variable', type=str, default='rho',
                        help='Variable')

    parser.add_argument('--starting_resolution', type=int, default=256,
                        help='Starting resolution (smallest resolution)')


    args = parser.parse_args()


    plot_info.add_additional_plot_parameters("basename", args.input_basename)

    plot_convergence_single_sample(args.input_basename, args.title, args.variable, args.starting_resolution, not args.not_zoom, args.compute_rate)

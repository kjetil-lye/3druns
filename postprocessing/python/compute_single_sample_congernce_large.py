import numpy as np
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['savefig.dpi'] = 600
import matplotlib.pyplot as plt
import sys
sys.path.append('../python')
import plot_info

latex_variables = {
    'rho' : '\\rho',
    'E'   : 'E',
}

def resolution_exists(basename, resolution):
    if not os.path.exists(basename.format(resolution=resolution)):
        return False

    try:
        load_plane(basename.format(resolution=resolution), 0, 'rho')
    except:
        return False

    return True


def load_plane(filename, plane, variable):
    with netCDF4.Dataset(filename) as f:
        return f.variables[f'sample_0_{variable}'][plane,:,:]

def plot_convergence_single_sample(basename, title, variable):
    resolution = 64

    resolutions = []
    errors = []
    while resolution_exists(basename, resolution):
        print(resolution)
        error = 0.0
        for plane in range(resolution):
            data_coarse = load_plane(basename.format(resolution=resolution), plane, variable)
            data_fine = np.repeat(np.repeat(load_plane(basename.format(resolution=2*resolution), plane, variable), 2, 0), 2, 1)

            error += np.sum(abs(data_coarse-data_fine))
        error /= resolution**3

        errors.append(error)
        resolutions.append(resolution)

        resolution *= 2

    resolutions = 2*np.array(resolutions)

    plt.loglog(resolutions, errors, '-o', basex=2, basey=2)
    plt.xlabel('Resolution ($N^3$)')
    ply.ylabel(f'Error ($||{latex_variables[variable]}^{{N}}-{latex_variables[variable]}^{{N/2}}||_{{L^1(D)}}$)')
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


    parser.add_argument('--variable', type=str, default='rho',
                        help='Variable')


    args = parser.parse_args()


    plot_info.add_additional_plot_parameters("basename", args.input_basename)

    plot_convergence_single_sample(args.input_basename, args.title, args.variable)
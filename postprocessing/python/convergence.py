import numpy as np
from plot_info import *
import netCDF4

def load(filename, variable):
    with netCDF4.Dataset(filename) as f:
        return f.variables[variable][:,:,:]


def statistics_convergence(filename_per_resolution, statistics_name, variable, setup):
    errors = []

    resolutions = np.array(sorted([r for r in filename_per_resolution.keys()]))
    d_prev = None
    for resolution in resolutions:
        filename =filename_per_resolution[resolution]
        d = load(filename, variable)

        if resolution > resolutions[0]:
            error = np.sum(np.abs(d - d_prev)/resolution**3)
            errors.append(error)
        d_prev = np.repeat(np.repeat(np.repeat(d, 2, 0), 2, 1), 2, 2)
        
        

    p = plt.loglog(resolutions[1:], errors, '-o', basex=2, basey=2,
                   label='Error {}'.format(statistics_name))
    poly = np.polyfit(np.log(resolutions[1:]), np.log(errors), 1)

    plt.loglog(resolutions[1:], np.exp(poly[1])*resolutions**poly[0],
               '--', label='$\\mathcal{{O}}(N^{{{:.2f}}})$'.format(poly[0]),
               color=p[0].get_color())

    plt.xlabel("Resolution ($N^3$)")
    
    plt.xticks(resolutions, ["${}^{{3}}$".format(r) for r in resolutions])
    plt.ylabel("Error ($||\\cdot||_{L^1(D)}$")
    plt.title("Convergence of {variable} ({statistic}, {setup})".format(variable = variable, statistic = statistics_name, setup = setup))
    plt.legend()

def plot_single_statistics(filename, statistic):
    # Need to implement paraview here
    pass

    
def plot_statistics_convergence(resolutions, basename, statistics, variable, setup):
    for statistic in statistics:
        filenames = {}

        for r in resolutions:
            filename = basename.format(resolution = r, statistic=statistic)

            filenames[r] = filename

        statistics_convergence(filenames, statistic, variable, setup)

        showAndSave("convergence_{setup}_{statistic}_{variable}".format(setup = setup, statistic = statistic, variable=variable))

        for r in resolutions:
            plot_single_statistics(filenames[r], statistic)
            showAndSave("single_level_{statistic}_{variable}".format(statistic = statistic, variable = variable))
            

import numpy as np
import latex_plots
import matplotlib
import matplotlib.pyplot as plt
import plot_info
from plot_info import *
import netCDF4
import scipy
import scipy.stats
import ot

from compressible_euler import latex_variables, conserved_variables

def load(filename, variable):
    with netCDF4.Dataset(filename) as f:
        for attr in f.ncattrs():
            plot_info.add_additional_plot_parameters(filename.replace("/", "_") + "_" + attr, f.getncattr(attr))
        return f.variables[variable][:,:,:]


def plot_3d(filename, variable, title):
    d = load(filename, variable)
    N = d.shape[0]
    
    x, y = np.mgrid[0:1:N*1j, 0:1:N*1j]
    Q = 3
    plt.figure(figsize=(16,16))
    for i in range(Q+1):
        
        plt.subplot(Q+1, 3, i*3+1)
       
        plt.pcolormesh(x, y, d[:,:, min(N-1, int((i/float(Q))*N))])
        plt.colorbar()
        plt.title("$z=\\frac{{{}}}{{{}}}$".format(i, Q))
        
        
        
        
        plt.subplot(Q+1, 3, i*3+2)
        
        plt.pcolormesh(x, y, d[:,min(N-1, int((i/float(Q))*N)),:])
        plt.colorbar()
        plt.title("$y=\\frac{{{}}}{{{}}}$".format(i, Q))
        
        
        
        
        plt.subplot(Q+1, 3, i*3+3)
        plt.pcolormesh(x, y, d[min(N-1, int((i/float(Q))*N)),:, :])
        plt.colorbar()
        plt.title("$x=\\frac{{{}}}{{{}}}$".format(i, Q))
        
    plt.tight_layout()
        
        
    plt.suptitle(title)
            
            
            
def single_sample_convergence(filename_per_resolution, sample, variable, setup):
    errors = []

    resolutions = np.array(sorted([r for r in filename_per_resolution.keys()]))
    d_prev = None
    for resolution in resolutions:
        filename =filename_per_resolution[resolution]
        d = load(filename, "sample_{}_{}".format(sample, variable))

        if resolution > resolutions[0]:
            error = np.sum(np.abs(d - d_prev)/resolution**3)
            errors.append(error)
        d_prev = np.repeat(np.repeat(np.repeat(d, 2, 0), 2, 1), 2, 2)
        
        

    p = plt.loglog(resolutions[1:], errors, '-o', basex=2, basey=2,
                   label='Error {}'.format(variable))
    poly = np.polyfit(np.log(resolutions[1:]), np.log(errors), 1)

    plt.loglog(resolutions[1:], np.exp(poly[1])*resolutions[1:]**poly[0],
               '--', label='$\\mathcal{{O}}(N^{{{:.2f}}})$'.format(poly[0]),
               color=p[0].get_color(), basex=2, basey=2)

    plt.xlabel("Resolution ($N^3$)")
    
    plt.xticks(resolutions[1:], ["${}^{{3}}$".format(r) for r in resolutions[1:]])
    plt.ylabel("Error ($||\\cdot||_{L^1(D)}$")
    plt.title("Convergence of {variable} (sample {sample}, {setup})".format(variable = variable, sample = sample, setup = setup))
    plt.legend()
    
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

    plt.loglog(resolutions[1:], np.exp(poly[1])*resolutions[1:]**poly[0],
               '--', label='$\\mathcal{{O}}(N^{{{:.2f}}})$'.format(poly[0]),
               color=p[0].get_color(),
               basex=2, basey=2)

    plt.xlabel("Resolution ($N^3$)")
    
    plt.xticks(resolutions[1:], ["${}^{{3}}$".format(r) for r in resolutions[1:]])
    plt.ylabel("Error ($||\\cdot||_{L^1(D)}$")
    plt.title("Convergence of {variable} ({statistic}, {setup})".format(variable = variable, statistic = statistics_name, setup = setup))
    plt.legend()

def plot_single_sample_convergence(resolutions, basename, sample, variable, setup):
    filenames = {}

    for r in resolutions:
        
        filename = basename.format(resolution = r)

        filenames[r] = filename

    single_sample_convergence(filenames, sample, variable, setup)

    showAndSave("convergence_single_sample_{setup}_{sample}_{variable}".format(setup = setup, sample = sample, variable=variable))

    #for r in resolutions:
    #    plot_single_statistics(filenames[r], statistic)
    #    #showAndSave("single_level_{statistic}_{variable}".format(statistic = statistic, variable = variable))
 

    
def plot_statistics_convergence(resolutions, basename, statistics, variable, setup):
    for statistic in statistics:
        filenames = {}

        for r in resolutions:
            filename = basename.format(resolution = r, statistic=statistic)

            filenames[r] = filename

        statistics_convergence(filenames, statistic, variable, setup)

        showAndSave("convergence_{setup}_{statistic}_{variable}".format(setup = setup, statistic = statistic, variable=variable))

        for r in resolutions:
            plot_3d(filenames[r], variable, "{} at ${}^{{3}}$".format(statistic, r))
            showAndSave("single_level_statistics_{setup}_{statistic}_{variable}_{r}".format(statistic = statistic, 
                        setup = setup,
                        variable = variable, r=r))

def get_number_of_samples(filename, variable):
    samples = 0
    with netCDF4.Dataset(filename) as f:
        for k in f.variables.keys():
            if variable in k:
                samples += 1

    return samples

def load_samples_point(filename, variable, i, j, k):
    samples = []

    with netCDF4.Dataset(filename) as f:
        for key in f.variables.keys():
            if variable in key:

                samples.append(f.variables[key][i,j,k])
    return np.array(samples)

def load_plane(filename, k, number_of_samples, variables):
    
    with netCDF4.Dataset(filename) as f:
        for attr in f.ncattrs():
            plot_info.add_additional_plot_parameters(filename.replace("/", "_") + "_" + attr, f.getncattr(attr))
        resolution = f.variables['sample_0_rho'].shape[0]
        
        samples = np.zeros((number_of_samples, resolution, resolution, len(variables)))
        for variable_index, variable in enumerate(variables):
            for sample in range(number_of_samples):
                key = f'sample_{sample}_{variable}'
                
                samples[sample,:,:,variable_index] = f.variables[key][k,:,:]
                
    return samples


def progress(part, total):
    message = "Computing done: {:.10f}%\r".format(float(part)/total*100.)
    sys.stdout.write(message)
    sys.stdout.flush()
    if isnotebook():
        try:
            with open("/dev/stdout", "w") as f:
                f.write(message)
                f.flush()
        except:
            pass
    

def wasserstein_1pt(filenames, title, reference_solution=False):
    # don't judge me for the next line
    resolutions = np.array(sorted(list([k for k in filenames.keys()])))

    errors = []
    
    number_of_variables = len(conserved_variables)
    
    if reference_solution:
        for r in resolutions[:-1]:
            max_resolution = resolutions[-1]
            weights_a = np.ones(max_resolution) / max_resolution
            weights_b = np.ones(max_resolution) / max_resolution
    
            wasserstein_error = 0.0
    
            for coarse_plane in range(r):
                d2 = load_plane(filenames[r], coarse_plane, max_resolution, conserved_variables)
                factor = max_resolution // r
                for fine_plane_local_index in range(factor):
                    fine_plane = coarse_plane * factor + fine_plane_local_index
                    
                    d1 = load_plane(filenames[max_resolution], fine_plane, max_resolution, conserved_variables)
            
                    for j in range(max_resolution):
                        for k in range(max_resolution):
        
        #                    d1 = load_samples_point(filenames[r], variable, i, j, k)
        #                    d2 = load_samples_point(filenames[r//2], variable, i//2, j//2, k//2)
                            distances = ot.dist(d1[:,j,k,:], d2[:,j//factor,k//factor,:], metric='euclidean')
                            emd_pairing = ot.emd(weights_a, weights_b, distances)
                            wasserstein_distance = np.sum(emd_pairing * distances)
                            wasserstein_error += wasserstein_distance
            wasserstein_error /= max_resolution**3
    
            errors.append(wasserstein_error)
            print()
            console_log("")
            console_log("Done with {}".format(r))
            
            
            plt.loglog(resolutions[:-1], errors, '-o', basex=2, basey=2)
        
    else:
        for r in resolutions[1:]:
            weights_a = np.ones(r) / r
            weights_b = np.ones(r) / r
    
            wasserstein_error = 0.0
    
            for i in range(r):
                progress(i, r)
                
                d1 = load_plane(filenames[r], i, r, conserved_variables)
                d2 = load_plane(filenames[r//2], i//2, r, conserved_variables)
                for j in range(r):
                    for k in range(r):
    
    #                    d1 = load_samples_point(filenames[r], variable, i, j, k)
    #                    d2 = load_samples_point(filenames[r//2], variable, i//2, j//2, k//2)
                        distances = ot.dist(d1[:,j,k,:], d2[:,j//2,k//2,:], metric='euclidean')
                        emd_pairing = ot.emd(weights_a, weights_b, distances)
                        wasserstein_distance = np.sum(emd_pairing * distances)
                        wasserstein_error += wasserstein_distance
            wasserstein_error /= r**3
    
            errors.append(wasserstein_error)
            print()
            console_log("")
            console_log("Done with {}".format(r))
            
    
        plt.loglog(resolutions[1:], errors, '-o', basex=2, basey=2)
    plt.xlabel("Resolution ($N^3$)")
    
    plt.xticks(resolutions[1:], ["${}^{{3}}$".format(r) for r in resolutions[1:]])
    
    filename_append = ''
    
    if reference_solution:
        filename_append = '_reference'
    
    saveData(f"wasserstein_1pt{filename_append}_{title}_all_errors", errors)
    saveData(f"wasserstein_1pt{filename_append}_{title}_all_resolutions", resolutions)
    
    if reference_solution:
        plt.ylabel(f"Error ($\\lVert W_1(\\nu^{{1,N}}, \\nu^{{1,{max_resolution}}})\\rVert_{{L^1(D)}}$")
    else:
        plt.ylabel("Error ($\\lVert W_1(\\nu^{1,N}, \\nu^{1,2 N })\\rVert_{L^1(D)}$")
    
    
    plt.title(f"One point $W_1$-convergence\n{title}")

        
        


def plot_wasserstein_convergence(resolutions, basename, title, reference_solution=False):
    filenames = {}

    for r in resolutions:
        filenames[r] = basename.format(resolution=r)
    
    wasserstein_1pt(filenames, title, reference_solution)
    
    if reference_solution:
        showAndSave(f"wasserstein_1pt_{title}_all_reference")
    else:
        showAndSave(f"wasserstein_1pt_{title}_all")
    




def wasserstein_1pt_comparison(filenames_a,
                               name_a,
                               filenames_b,
                               name_b,
                               variable, title):
    # don't judge me for the next line
    resolutions = np.array(sorted(list([k for k in filenames_a.keys()])))

    errors = []
    for r in resolutions:

        wasserstein_error = 0.0

        for i in range(r):
            progress(i, r)
            d1 = load_plane(filenames_a[r], variable, i)
            d2 = load_plane(filenames_b[r], variable, i)
            for j in range(r):
                for k in range(r):
                    wasserstein_error += scipy.stats.wasserstein_distance(d1[:,j,k], d2[:,j,k])
        wasserstein_error /= r**3

        errors.append(wasserstein_error)
        print()
        console_log("")
        console_log("Done with {}".format(r))
    plt.loglog(resolutions, errors, '-o', basex=2, basey=2)
    plt.xlabel("Resolution ($N^3$)")
    
    plt.xticks(resolutions, ["${}^{{3}}$".format(r) for r in resolutions])
    
    saveData(f"wasserstein_1pt_comparison_{title}_{name_a}_{name_b}_{variable}_errors", errors)
    saveData(f"wasserstein_1pt_comparison_{title}_{name_a}_{name_b}__{variable}_resolutions", resolutions)
    plt.ylabel(f"Error ($\\lVert W_1(\\nu^{{1,N}}_{{\\mathrm{{{name_a}}}}}, \\nu^{{1,N }}_{{\\mathrm{{{name_b}}}}})\\rVert_{L^1(D)}$")
    plt.title(f"One point $W_1$-convergence\n{title}\n"
              f"Comparing {name_a} and {name_b}\n"
              f"Variable: ${variable}$")



def plot_wasserstein_convergence_comparison(resolutions, 
                                            basename_a,
                                            name_a,
                                            basename_b,
                                            name_b, 
                                            variable, title):
    filenames_a = {}
    filenames_b = {}

    for r in resolutions:
        filenames_a[r] = basename_a.format(resolution=r)
        filenames_b[r] = basename_b.format(resolution=r)
    
    wasserstein_1pt_comparison(filenames_a,
                               name_a,
                               filenames_b, 
                               name_b, 
                               variable, title)
    
    showAndSave(f"wasserstein_1pt_comparison_{title}_{name_a}_{name_b}_{variable}")
    

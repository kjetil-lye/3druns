import numpy as np
from plot_info import *
import netCDF4
import scipy
import scipy.stats

def load(filename, variable):
    with netCDF4.Dataset(filename) as f:
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
                d = f.variables[key][:,:,:]
                samples.append(d[i,j,k])
    return np.array(samples)

def progress(part, total):
    message = "Computing done: {:.2f}%\r".format(part/total*100.)
    sys.stdout.write(message)
    sys.stdout.flush()
    if isnotebook():
        try:
            with open("/dev/stdout", "w") as f:
                f.write(message)
                f.flush()
        except:
            pass
    

def wasserstein_1pt(filenames, variable, setup):
    # don't judge me for the next line
    resolutions = np.array(sorted(list([k for k in filenames.keys()])))

    errors = []
    for r in resolutions[1:]:

        wasserstein_error = 0.0

        for i in range(r):
            for j in range(r):
                for k in range(r):
                    progress(i*r**2 + j*r +  k, r**3)
                    d1 = load_samples_point(filenames[r], variable, i, j, k)
                    d2 = load_samples_point(filenames[r//2], variable, i//2, j//2, k//2)

                    wasserstein_error += scipy.stats.wasserstein_distance(d1, d2)
        wasserstein_error /= r**3

        errors.append(wasserstein_error)
        print()
        console_log("")
        console_log("Done with {}".format(r))
    plt.loglog(errors, wasserstein_error, '-o')
    plt.xlabel("Resolution ($N^3$)")
    
    plt.xticks(resolutions[1:], ["${}^{{3}}$".format(r) for r in resolutions[1:]])
    plt.ylabel("Error ($||W_1(\\nu^{1,N}, \\nu^{1,2\\cdot N })||_{L^1(D)}$")
    plt.title("One point $W_1$-convergence of {variable} ({setup})".format(variable = variable, setup = setup))

        
        


def plot_wasserstein_convergence(resolutions, basename, variable, setup):
    filenames = {}

    for r in resolutions:
        filenames[r] = basename.format(resolution=r)
    
    wasserstein_1pt(filenames, variable, setup)
    showAndSave("wasserstein_1pt_{setup}_{variable}".format(setup=setup, variable=variable))
    

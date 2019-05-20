import numpy as np
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['savefig.dpi'] = 600

import matplotlib.pyplot as plt

import sys
sys.path.append('../python')
from plot_info import showAndSave, savePlot

import netCDF4
import matplotlib2tikz
import os
import h5py
import ot
import sys
import scipy
import scipy.stats
import plot_info

def load_sample(filename, sample, i,j,k):
    with netCDF4.Dataset(filename) as f:
        d = f.variables['sample_{}_rho'.format(sample)]

        

        return d[i,j,k]
    
    

def wasserstein_point2_fast(a, b, xs, xt):
    """
    Computes the Wasserstein distance for a single point in the spatain domain
    """
    



    M = ot.dist(xs, xt, metric='euclidean')
    G0 = ot.emd(a,b,M)

    return np.sum(G0*M)

def wasserstein2pt_fast(filename_a, filename_b, N):
    """
    Approximate the L^1(W_1) distance (||W_1(nu1, nu2)||_{L^1})
    """

    
    a = np.ones(N)/N
    b = np.ones(N)/N
    xs = np.zeros((N,2))
    xt = np.zeros((N,2))
    distance = 0
    
    N_points = 10
    
    points = np.linspace(0, 1, N_points)

   
    for nx, x in enumerate(points):
        for ny, y in enumerate(points):
            
            for nz, z in enumerate(points):
                sys.stdout.write(nx*N**2 + ny*N + nz)
                sys.stdout.flush()
                for xp in points:
                    for yp in points:
                        for zp in points:
                            for sample in range(N):
                                
                        
                                i = int(x*N)
                                j = int(y*N)
                                k = int(z*N)
                                
                                ip = int(xp*N)
                                jp = int(yp*N)
                                kp = int(zp*N)
                                
                                xs[sample, 0] = load_sample(filename_a, sample, i, j, k)
                                xs[sample, 1] = load_sample(filename_a, sample,ip, jp, kp)
                                
                                xt[sample, 0] = load_sample(filename_a, sample, i//2, j//2, k//2)
                                xt[sample, 1] = load_sample(filename_a, sample, ip//2, jp//2, kp//2)
                                
                                distance += wasserstein_point2_fast(a, b, xs, xt)

    print("Done")
    
    return distance / len(points)**6





def plotWassersteinConvergence(name, basename, resolutions):
    wasserstein2pterrors = []
    for r in resolutions[1:]:
        print(r)
        filename = basename % r
        filename_coarse = basename % int(r/2)
        

        wasserstein2pterrors.append(wasserstein2pt_fast(filename, filename_coarse, r))
        print("wasserstein2pterrors=%s" % wasserstein2pterrors)
    

    plt.loglog(resolutions[1:], wasserstein2pterrors, '-o', basex=2, basey=2)
    plt.xlabel("Resolution")
    plt.xticks(resolutions[1:], ['${r} \\times {r}$'.format(r=r) for r in resolutions[1:]])
    plt.ylabel('$||W_1(\\nu^{2, \\Delta x}, \\nu^{2,\\Delta x/2})||_{L^1(D\\times D)}$')
    plt.title("Wasserstein convergence for %s\nfor second correlation marginal"%name)
    showAndSave('%s_wasserstein_convergence_2pt' % name)
    
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print("Usage\n\tpython{} basename name\n".format(sys.argv[0]))
    basename = sys.argv[1]
    name = sys.argv[2]
    plot_info.set_additional_plot_parameters("basename", basename)
    resolutions [64, 128, 256, 512]
    plotWassersteinConvergence(name, basename, resolutions)

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

def load_plane(filename, sample, plane):
    with netCDF4.Dataset(filename) as f:
        d = f.variables['sample_{}_rho'.format(sample)]

        N = d.shape[0]

        k = int(plane*N)

        return d[:,:,k]
    
    

def wasserstein_point2_fast(data1, data2, i, j, ip, jp, a, b, xs, xt):
    """
    Computes the Wasserstein distance for a single point in the spatain domain
    """
    

    xs[:,0] = data1[i,j,:]
    xs[:,1] = data1[ip, jp, :]

    xt[:,0] = data2[i,j, :]
    xt[:,1] = data2[ip, jp, :]


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
    length = 1.0/N_points
    points = np.linspace(0, 1, N_points)

    data1 = np.zeros((N,N,N))
    data2 = np.zeros((N,N,N))
    for plane in points:
        for sample in range(N):
            data1[:,:,sample] = load_plane(filename_a, sample, plane)
            data2[:,:,sample] = np.repeat(np.repeat(load_plane(filename_b, sample, plane), 2, 0), 2, 1)
        
        for x in points:
            for y in points:
                for xp in points:
                    for yp in points:
                        
                        i = int(x*N)
                        j = int(y*N)
                        ip = int(xp*N)
                        jp = int(yp*N)
                        distance += wasserstein_point2_fast(data1, data2, i,j, ip, jp, a, b, xs, xt)


    
    return distance / len(points)**6





def plotWassersteinConvergence(name, basename, resolutions):
    wasserstein2pterrors = []
    for r in resolutions[1:]:
        filename = basename % r
        filename_coarse = basename % int(r/2)
        

        wasserstein2pterrors.append(wasserstein2pt_fast(filename, filename_course, r))
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

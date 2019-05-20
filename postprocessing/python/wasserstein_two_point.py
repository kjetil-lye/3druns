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

def load_samples_plane(filename, N, kp, upscale_resolution):
    data = np.zeros((upscale_resolution, upscale_resolution, N))
    with netCDF4.Dataset(filename) as f:
        for k in range(N):
            d = f.variables['sample_{}_rho'.format(k)][kp,:,:]
            
            while d.shape[1] < upscale_resolution:
                d = np.repeat(np.repeat(d,2,0), 2, 1)
            
            data[:,:,k] = d
            
    return data
            
      

def load_sample(filename, sample, i,j,k):
    with netCDF4.Dataset(filename) as f:
        d = f.variables['sample_{}_rho'.format(sample)]

        

        return d[i,j,k]
    
def load_samples(filename, N, i, j, k):
    data = np.zeros(N)
    for k in range(N):
        data[k] = load_sample(filename, N, i, j, k)
    return data
    
    

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
    
    points = 1.0/N_points * np.arange(0,N_points)

   
    for nx, x in enumerate(points):
        for ny, y in enumerate(points):
            
            for nz, z in enumerate(points):
                i = int(x*N)
                j = int(y*N)
                k = int(z*N)
                
                xs[:, 0] = load_samples(filename_a, N, i, j, k)
                xt[:, 0] = np.repeat(load_samples(filename_b, N//2, i//2, j//2, k//2), 2, 0)
                
                for nzp, zp in enumerate(points):
                    kp = int(zp*N)
                    samples_plane_a = load_samples_plane(filename_a, N, kp, N)
                    samples_plane_b = np.repeat(load_samples_plane(filename_a, N//2, kp//2, N), 2, 2)
                    
                    for nxp, xp in enumerate(points):
                        for nyp, yp in enumerate(points):
                        
                           
                            ip = int(xp*N)
                            jp = int(yp*N)
                                
                                
                                
                                
                           
                            xs[:, 1] = samples_plane_a[ip, jp,:]
                                
                            
                            xt[:, 1] = samples_plane_b[ip, jp, :]
                            
                            
                            sys.stdout.write('{}\r'.format(str(nxp*N**2 + nyp*N + nzp)))
                            sys.stdout.flush()
                                
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
        exit(0)
    basename = sys.argv[1]
    name = sys.argv[2]
    plot_info.add_additional_plot_parameters("basename", basename)
    resolutions =  [64, 128, 256, 512]
    plotWassersteinConvergence(name, basename, resolutions)

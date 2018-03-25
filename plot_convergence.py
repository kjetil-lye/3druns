from numpy import *
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import sys
import netCDF4

for t in range(11):
    errors = []
    resolutions = [64,128,256,512,1024]

    for r in resolutions:
        with netCDF4.Dataset('convergence/N{}/tg_perturbed_{}.nc'.format(r, t)) as f:
            sample = 0
            d = f.variables['sample_%d_rho' % sample][:,:,:]

            N = d.shape[0]

            for k in range(5):
                dl = d[int(k*N/5),:,:]
                x,y = mgrid[0:1:N*1j, 0:1:N*1j]
                plt.pcolormesh(x,y,dl)
                plt.colorbar()
                plt.savefig('img/convergence_perturbed_%d_%d_%d.png' % (t,r,k))
                plt.close('all')
            if r > resolutions[0]:
                errors.append(sum(abs(d-dPrev))/r**3)
            dPrev = repeat(repeat(repeat(d,2,0),2,1),2,2)
    plt.loglog(resolutions[1:], errors, '-o')
    plt.title('$L^1$ convergence at $t={}$'.format(t/10.*4))
    plt.xlabel('Resolution (number of cells in one direction)')
    plt.ylabel('Error ($||\\cdot||_{L^1}$)')
    plt.savefig('img/convergence_perturbed_%d.png' % t)
    plt.close('all')
            


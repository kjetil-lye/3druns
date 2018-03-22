from numpy import *
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import sys
import netCDF4

with netCDF4.Dataset(sys.argv[1]) as f:
    d = f.variables['sample_0_rho'][:,:,:]

    N = d.shape[0]

    for k in range(5):
        dl = d[int(k*N/5),:,:]
        x,y = mgrid[0:1:N*1j, 0:1:N*1j]
        plt.pcolormesh(x,y,dl)
        plt.colorbar()
        plt.savefig('img/%s_%d.png' % (sys.argv[1].replace('.nc', ''), k))
        plt.close('all')


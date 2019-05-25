import netCDF4
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import numpy as np
import sys

if __name__ == '__main__':
    inname = sys.argv[1]
    M = 4
    fig, axes = plt.subplots(M, 3, sharex='all', sharey='all', figsize=(32,32))
    fig.suptitle(inname, fontsize=30)
    with netCDF4.Dataset(inname) as f:
        
        N = f.variables['sample_0_rho'].shape[0]
        x, y = np.mgrid[0:1:N*1j, 0:1:N*1j]

        for j in range(0, M):
            ax = axes[j,0]
            d = f.variables['sample_0_rho'][:,:,(j*N)//M]

            im = ax.pcolormesh(x, y, d)
            try:
                ax.set_xlabel('$x$')
                ax.set_ylabel('$y$')
            except:
                pass
            fig.colorbar(im, ax=ax)
            ax.set_title("Fixing $z={}$".format(j/M), fontsize=20)
            
            ax = axes[j, 1]
            d = f.variables['sample_0_rho'][:,(j*N)//M,:]

            im = ax.pcolormesh(x, y, d)
            try:
                ax.set_xlabel('$x$')
                ax.set_ylabel('$y$')
            except:
                pass
            fig.colorbar(im, ax=ax)
            ax.set_title("Fixing $y={}$".format(j/M), fontsize=20)

            ax = axes[j, 2]
            d = f.variables['sample_0_rho'][(j*N)//M, :, :]

            img = ax.pcolormesh(x, y, d)
            try:
                ax.set_xlabel('$x$')
                ax.set_ylabel('$y$')
            except:
                pass
            fig.colorbar(im, ax=ax)
            ax.set_title("Fixing $x={}$".format(j/M), fontsize=20)

        plt.savefig(inname.replace('.nc', '.png'))

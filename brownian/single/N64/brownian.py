import numpy as np
from numpy import *

class RandomVariable(object):
    def __init__(self, X):
        self.X = X
        self.i = -1

    def __call__(self):
        self.i += 1
        return self.X[self.i]


def variancefBm(H,n):
    return sqrt((1-2**(2*H-2))/(2**(2*n*H)))

# Helper functions to deal with indexing, could not find a better way?
def at(vector, index):
    return vector[index[0], index[1], index[2]]
# Helper functions to deal with indexing, could not find a better way?
def set_value(vector, index, value):
    vector[index[0], index[1], index[2]] = value
    
def brownian(Y, nx, ny, nz, x, y, z, Nx, Ny, Nz):
    u = zeros((nx, ny, nz))
    for i in range(nx):
        for j in range(ny):
            for k in range(nz):
                u[i,j,k] = np.sum(Y * np.sin((Nx-1/2)*np.pi*x[i,j,k]) * \
                                   np.sin((Ny-1/2)*np.pi*y[i,j,k]) * \
                                   np.sin((Nz-1/2)*np.pi*z[i,j,k]) \
                                          / ((Nx-1.0/2.0)*np.pi*(Ny-1.0/2.0)*np.pi*(Nz-1.0/2.0)*np.pi))

    return u
    

# Using tensor product Karuhnen Loewe expansion of Brownian motion
def init_global(rho, ux, uy, p, nx, ny, nz, ax, ay, az, bx, by, bz):
    Y1 = X[:nx*ny*ny].reshape(nx, ny, nz)
    Y2 = X[nx*ny*ny:].reshape(nx, ny, nz)
    Y3 = X[2*nx*ny*ny:].reshape(nx, ny, nz)
    x, y, z = np.mgrid[ax:bx:nx*1j, ay:by:ny*1j, az:bz:nz*1j]
    Nx, Ny, Nz = np.meshgrid(np.arange(0,ny), np.arange(0,ny), np.arange(0, nz))

    ux[:,:,:] = brownian(Y1, nx, ny, nz, x,y,z, Nx, Ny, Nz)
    uy[:,:,:] = brownian(Y2, nx, ny, nz, x,y,z, Nx, Ny, Nz)
    uz[:,:,:] = brownian(Y3, nx, ny, nz, x,y,z, Nx, Ny, Nz)
    rho[:,:,:] = 4*ones_like(rho[:,:,:])
    p[:,:,:] = 2.5*ones_like(rho[:,:,:])




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
    
    
def fBm(N, H, rand):
    n = log2(N)
    print(n)
    d = zeros((N+1,N+1, N+1))
    if N==1:
        return d
    else:
        dPrev = fBm(N//2,H,rand)
        
        for i in range(0,N//2):
            for j in range(0,N//2):
                for k in range(0,N//2):
                    d[2*i,2*j, 2*k] = dPrev[i,j,k]
        
        
        for i in range(0,N//2,1):
            for j in range(0,N//2,1):
                for k in range(0,N//2,1):
                    for side in range(6):
                        position = np.array([i,j,k])
                        e1 = np.array([side<2,  side>=2 and side<4, side>=4])
                        e2 = np.array([(side>=2 and side<4), side >= 4, side < 2])
                        
                    
        
                        set_value(d, 2*position + e1, 
                                  0.5*(at(d, 2 * position)+at(d, 2 * (position + e1)))+variancefBm(H,n)*rand())
    
                        set_value(d, 2*position + e2, 
                                  0.5*(at(d, 2 * position) + at(d, 2*(position + e2)))+variancefBm(H,n)*rand())
        
                        # We will have some duplicates here... but it is ok
                        # doesn't affect runtime all that much, and we focus more 
                        # on perfectly correct results
                        #set_value(d, 2*position + 2 * e1 + e2,
                        #    0.5*(at(d,2 * position + 2 * e1) +\
                        #         at(d, 2 * (position + e1 + e2)))+\
                        #variancefBm(H,n)*rand())
    
                        #set_value(d, 2*position + e1 + 2 * e2, 0.5*(at(d, 2 * position + 2 * e2) 
                        #    + at(d, 2*(position + e1 + e2)))+variancefBm(H,n)*rand())
        
                    
                        set_value(d, 2*position + e1 + e2, 1.0/4.0*(at(d, position) + \
                                        at(d, position + 2*e1) + \
                                        at(d, position + 2*e2) + \
                                        at(d, position + 2 * e2 + 2*e1)) \
                                       +variancefBm(H,n)*rand())
                    d[2*i +1, 2*j+1, 2*k + 1] = 1.0 / 8.0 * (\
                           d[2*i    , 2*j    , 2*k    ]\
                         + d[2*i + 1, 2*j    , 2*k    ]\
                         + d[2*i + 1, 2*j + 1, 2*k    ]\
                         + d[2*i + 1, 2*j + 1, 2*k + 1]\
                         + d[2*i + 1, 2*j    , 2*k + 1]\
                         + d[2*i    , 2*j + 1, 2*k    ]\
                         + d[2*i    , 2*j + 1, 2*k + 1]\
                         + d[2*i    , 2*j    , 2*k + 1])\
                         +variancefBm(H,n)*rand()

        return d


# This is found in the paper
# Brouste, A., Istas, J., & Lambert-Lacroix, S. (2007).
#  On Fractional Gaussian Random Fields Simulations. Journal of Statistical Software, 23(1), 1–23.
#  http://doi.org/http://dx.doi.org/10.18637/jss.v023.i01
# in the section 2.3

def init_global(rho, ux, uy, p, nx, ny, nz, ax, ay, az, bx, by, bz):
    
    dux = fBm(nx, HURST, RandomVariable(X[:4*nx*nx*nx]))
    duy= fBm(nx, HURST, RandomVariable(X[4*nx*nx*nx:]))
    duz= fBm(nx, HURST, RandomVariable(X[8*nx*nx*nx:]))
    
    rho[:,:,:] = 4*ones_like(rho[:,:,:])
    ux[:,:,:] = dux[:-1,:-1,:-1]
    uy[:,:,:] = duy[:-1,:-1,:-1]
    uz[:,:,:] = duz[:-1,:-1,:-1]
    p[:,:,:] = 2.5*ones_like(rho[:,:,:])




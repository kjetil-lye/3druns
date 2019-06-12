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

def init_global(rho, ux, uy, uz, p, nx, ny, nz, ax, ay, az, bx, by, bz):

    ### WARNING:
    ### THE CURRENT IMPLEMENTATION IS SUBOPTIMAL!!!
    ### WE GENERATE THE WHOLE FIELD FOR EVERY NODE.
    ### THIS IS SIMPLY DONE FOR SIMPLICITY (AT MOST
    ### WE RUN 8 NODES FOR THIS CONFIG, HENCE NOT A BIG ISSUE)
    total_nx = int(nx/(bx-ax))
    total_ny = int(ny/(by-ay))
    total_nz = int(nz/(bz-az))
    
    dux = fBm(total_nx, hurst_index, RandomVariable(X[:4*total_nx**3]))
    duy= fBm(total_nx, hurst_index, RandomVariable(X[4*total_nx**3:8*total_nx**3]))
    duz= fBm(total_nx, hurst_index, RandomVariable(X[8*total_nx**3:]))

    start_x = int(ax*total_nx)
    end_x = int(bx*total_nx)
    
    start_y = int(ay*total_ny)
    end_y = int(by*total_ny)

    start_z = int(az*total_nz)
    end_z = int(bz*total_nz)

    output = False
    if output:
        print("total_x={total_x}\ntotal_y={total_y}\ntotal_z={total_z}".format(
            total_x=total_nx, total_y=total_ny, total_z=total_nz))
        print("start_x={start_x}\nstart_y={start_y}\nstart_z={start_z}".format(
            start_x=start_x, start_y=start_y, start_z=start_z))
        print("end_x={end_x}\nend_y={end_y}\nend_z={end_z}".format(
            end_x=end_x, end_y=end_y, end_z=end_z))
    rho[:,:,:] = 4*ones_like(rho)
    ux[:,:,:] = dux[start_x:end_x,start_y:end_y,start_z:end_z]
    uy[:,:,:] = duy[start_x:end_x,start_y:end_y,start_z:end_z]
    uz[:,:,:] = duz[start_x:end_x,start_y:end_y,start_z:end_z]
    p[:,:,:] = 2.5*ones_like(rho[:,:,:])





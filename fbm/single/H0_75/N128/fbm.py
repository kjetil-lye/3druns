import scipy.stats
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

    # X is uniform, ppf is the inverse of the normal pdf, so that means Y will uniform
    Y = scipy.stats.norm.ppf(X)

    number_of_parameters=(total_nx-1)**3
    # uses fbmpy at https://github.com/alsvinn/fractional_brownian_motion
    # Needs to have a newer version of alsvinn (at or after 2019-06-17)
    dux = fbmpy.fractional_brownian_bridge_3d(hurst_index, total_nx, Y[:number_of_parameters]).reshape(total_nx+1,total_nx+1,total_nx+1)
    duy = fbmpy.fractional_brownian_bridge_3d(hurst_index, total_nx, Y[number_of_parameters:2*number_of_parameters]).reshape(total_nx+1,total_nx+1,total_nx+1)
    duz = fbmpy.fractional_brownian_bridge_3d(hurst_index, total_nx, Y[2*number_of_parameters:3*number_of_parameters]).reshape(total_nx+1,total_nx+1,total_nx+1)

    start_x = int(ax*total_nx)
    end_x = int(bx*total_nx)
    
    start_y = int(ay*total_ny)
    end_y = int(by*total_ny)

    start_z = int(az*total_nz)
    end_z = int(bz*total_nz)

    rho[:,:,:] = 4*ones_like(rho)
    ux[:,:,:] = dux[start_x:end_x,start_y:end_y,start_z:end_z]
    uy[:,:,:] = duy[start_x:end_x,start_y:end_y,start_z:end_z]
    uz[:,:,:] = duz[start_x:end_x,start_y:end_y,start_z:end_z]
    p[:,:,:] = 2.5*ones_like(rho[:,:,:])





import sys
sys.path.append('../python')
import numpy as np
import convergence
if __name__ == '__main__':

    

    basename = sys.argv[1]
    if len(sys.argv) > 2:
        starting_resolution = int(sys.argv[2])
    else:
        starting_resolution = 64

    resolutions = 2**np.arange(int(np.log2(starting_resolution)), 10)
    print(resolutions)
    variable = 'rho'
    setup = basename.format(resolution='res')

    convergence.plot_wasserstein_convergence(resolutions, basename, variable, setup)

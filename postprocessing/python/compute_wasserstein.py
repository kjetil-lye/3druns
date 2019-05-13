import sys
sys.path.append('../python')
import convergence
if __name__ == '__main__':

    resolutions=[64, 128, 256, 512]
    basename = sys.argv[1]
    variable = 'rho'
    setup = basename.format(resolution='res')

    convergence.plot_wasserstein_convergence(resolutions, basename, variable, setup)

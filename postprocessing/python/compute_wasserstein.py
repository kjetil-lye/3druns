import sys

sys.path.append('../python')
import plot_info
import numpy as np
import convergence
if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser(description="""
Computes the 1 pt wasserstein convergence
            """)

    parser.add_argument('--input_basename', type=str, required=True,                        help='Input filename (should have a format string {resolution})')

    parser.add_argument('--title', type=str, required=True,
                        help='Title of plot')


    parser.add_argument('--variable', type=str, default='rho',
                        help='Variable')

    parser.add_argument('--starting_resolution', type=int, default=32,
                        help='Starting resolution (smallest resolution)')

    args = parser.parse_args()


    basename = args.input_basename
    starting_resolution = args.starting_resolution
    
    resolutions = 2**np.arange(int(np.log2(starting_resolution)), 10)
    print(resolutions)
    variable = args.variable
    
    
    plot_info.add_additional_plot_parameters("basename", args.input_basename)

    convergence.plot_wasserstein_convergence(resolutions, basename, variable, args.title)

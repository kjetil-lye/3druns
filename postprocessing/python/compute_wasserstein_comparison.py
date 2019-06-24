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

    parser.add_argument('--title', type=str, required=True,
                        help='Title of plot')
    
    parser.add_argument('--input_basename_a', type=str, required=True,     
                        help='Input filename first (should have a format string {resolution})')
    
    parser.add_argument('--input_basename_b', type=str, required=True,     
                        help='Input filename first (should have a format string {resolution})')
    
    parser.add_argument('--name_b', type=str, required=True,     
                        help='Short descriptive name of basename_b (eg. "float")')
    
    parser.add_argument('--name_a', type=str, required=True,     
                        help='Short descriptive name of basename_a (eg. "double")')

    parser.add_argument('--variable', type=str, default='rho',
                        help='Variable')

    parser.add_argument('--starting_resolution', type=int, default=32,
                        help='Starting resolution (smallest resolution)')

    args = parser.parse_args()


    starting_resolution = args.starting_resolution
    
    resolutions = 2**np.arange(int(np.log2(starting_resolution)), 10)
    variable = args.variable


    plot_info.add_additional_plot_parameters("basename_a", args.input_basename_a)
    plot_info.add_additional_plot_parameters("basename_b", args.input_basename_b)
    convergence.plot_wasserstein_convergence_comparison(resolutions, 
                                                        args.input_basename_a,
                                                        args.name_a,
                                                        args.input_basename_b,
                                                        args.name_b,
                                                        variable, args.title)

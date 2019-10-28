"""
Computes the wasserstein distance between two files
"""
import mpi4py
from mpi4py import MPI
import netCDF4
import ot
import numpy as np
from compressible_euler import conserved_variables

# We are not going to plot, but we will save data
import plot_info
from convergence import timeit, wasserstein_inner_compute

def get_rank_global():
    comm = MPI.COMM_WORLD
    return comm.Get_rank()

def get_global_size():
    comm = MPI.COMM_WORLD
    return comm.Get_size()

def get_resolution(filename):
    with netCDF4.Dataset(filename) as f:
        return f.variables['sample_0_rho'].shape[0]
    

@timeit
def load_plane_line(filename, start_y, end_y, start_z, end_z, number_of_samples, variables):
    
    with netCDF4.Dataset(filename) as f:
        for attr in f.ncattrs():
            plot_info.add_additional_plot_parameters(filename.replace("/", "_") + "_" + attr, f.getncattr(attr))
        resolution = f.variables['sample_0_rho'].shape[0]
        
        length_z = end_z - start_z
        length_y = end_y - start_y
        length_x = resolution
        samples = np.zeros((number_of_samples, length_z, length_y, length_x, len(variables)))
        for variable_index, variable in enumerate(variables):
            for sample in range(number_of_samples):
                key = f'sample_{sample}_{variable}'
                
                samples[sample,:,:,:,variable_index] = f.variables[key][start_z:end_z,start_y:end_y,:]
                
    return samples

def get_node_z_y_ranges(multi_y, multi_z, resolution):
    rank = get_rank_global()
    
    size = get_global_size()
    
    rank_z = rank // multi_y
    rank_y = rank % multi_y
    
    number_of_lines_per_node = resolution // multi_y
    number_of_planes_per_node = resolution // multi_z
    
    start_y = rank_y * number_of_lines_per_node    
    end_y = (rank_y + 1) * number_of_lines_per_node
    
    start_z = rank_z * number_of_planes_per_node    
    end_z = (rank_z  + 1) * number_of_planes_per_node

    return start_y, end_y, start_z, end_z

def compute_wasserstein_one_point(file_a, file_b, multi_y, multi_z):
    resolution_a = get_resolution(file_a)
    resolution_b = get_resolution(file_b)
    
    resolution = max(resolution_a, resolution_b)
    
    if resolution_a > resolution_b:
        file_a, file_b = file_b, file_a
        resolution_a, resolution_b = resolution_b, resolution_a
        
    factor = resolution_b // resolution_a
    
    start_y, end_y, start_z, end_z = get_node_z_y_ranges(multi_y, multi_z, resolution)
    
    data_a = load_plane_line(file_a,
                             start_y // factor, 
                             end_y // factor,
                             start_z // factor,
                             end_z // factor,
                             resolution, 
                             conserved_variables)
    
    data_b = load_plane_line(file_b,
                             start_y, 
                             end_y,
                             start_z,
                             end_z,
                             resolution, 
                             conserved_variables)
    
    wasserstein_distance_sum = 0.0
    weights_a = np.ones(resolution) / resolution
    weights_b = np.ones(resolution) / resolution
    
    for z in range(end_z-start_z):
        for y in range(end_y-start_y):
            for x in range(resolution):
                distances = ot.dist(data_a[:,z//factor, y//factor,x//factor,:],
                                    data_b[:,z, y, x,:], metric='euclidean')
                            
                emd_pairing = wasserstein_inner_compute(weights_a, weights_b, distances)
                wasserstein_distance = np.sum(emd_pairing * distances)
                wasserstein_distance_sum += wasserstein_distance

    return wasserstein_distance_sum / resolution**3
    
def is_power_of_two(n):
    """ see https://stackoverflow.com/a/57027610 """
    return (n != 0) and (n & (n-1) == 0)
    
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="""
Computes the 1 pt wasserstein distance between two files
            """)

    parser.add_argument('--file_a', type=str, required=True,  
                        help='first file')

    parser.add_argument('--file_b', type=str, required=True,  
                        help='second file')


    parser.add_argument('--multi_y', type=int, required=True,
                     help='Number of processes in y direction')
    
    parser.add_argument('--multi_z', type=int, required=True,
                     help='Number of processes in z direction')
    
    parser.add_argument('--outfile', type=str, required=True,
                        help='Name of output file')
    
    

    args = parser.parse_args()
    
    mpi_size = get_global_size()
    
    if args.multi_z * args.multi_y != mpi_size:
        raise Exception(f'Wrong number of mpi processes given.\n\tGiven: {mpi_size}\n\tExpected: multi_z*multi_y = {args.multi_z} * {args.multi_y} = {args.multi_z * args.multi_y}\n')
    
    
    # maybe these two next checks are too strict, but wanted to be on the safe side
    if not is_power_of_two(args.multi_y):
        raise Exception(f'multi_y must be power of 2, given {args.multi_y}')

    if not is_power_of_two(args.multi_z):
        raise Exception(f'multi_z must be power of 2, given {args.multi_z}')
        
    wasserstein = compute_wasserstein_one_point(args.file_a, args.file_b, args.multi_y, args.multi_z)
    comm = MPI.COMM_WORLD
    sum_distance = comm.reduce(wasserstein, op=MPI.SUM)
    
    if get_rank_global() == 0:
        plot_info.saveData(args.outfile, sum_distance)
    

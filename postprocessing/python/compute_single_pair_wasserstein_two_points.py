"""
Computes the wasserstein distance between two files
"""
import mpi4py
from mpi4py import MPI
import netCDF4
import ot
import numpy as np
import copy

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
def load_points(filename, points, number_of_samples, variables):
    
    with netCDF4.Dataset(filename) as f:
        for attr in f.ncattrs():
            plot_info.add_additional_plot_parameters(filename.replace("/", "_") + "_" + attr, f.getncattr(attr))
        resolution = f.variables['sample_0_rho'].shape[0]
        
        samples = np.zeros((number_of_samples, len(points), len(variables)))
        for variable_index, variable in enumerate(variables):
            for sample in range(number_of_samples):
                key = f'sample_{sample}_{variable}'
                for point_index, point in enumerate(points):
                    samples[sample,point_index,variable_index] = f.variables[key][point[0], point[1], point[2]]
                
    return samples

@timeit
def add_all_points(points, point, dimension, number_of_points_per_dimension, resolution):
    if dimension == 0:
        points.append(point)
        return
    else:
        
        for point_index in range(number_of_points_per_dimension):
            temp_point = copy.deepcopy(point)
            temp_point.append(int(point_index*resolution/number_of_points_per_dimension))
            add_all_points(points, temp_point, dimension-1, number_of_points_per_dimension, resolution)
    
@timeit
def get_node_points(resolution, number_of_points_per_direction):
    rank = get_rank_global()
    
    size = get_global_size()
    dimension = 2*3
    
    number_of_points_per_node = max(1, number_of_points_per_direction**dimension // size)

    assert(number_of_points_per_node * size == number_of_points_per_direction**dimension)
    points_in_one_direction = np.arange(0, number_of_points_per_direction)

    all_points = []


    add_all_points(all_points, [], dimension, number_of_points_per_direction, resolution)

    start_index = rank * number_of_points_per_node
    end_index = (rank+1) * number_of_points_per_node

    
    return all_points[start_index:end_index]

def compute_wasserstein_two_points(file_a, file_b, number_of_points_per_direction):
    resolution_a = get_resolution(file_a)
    resolution_b = get_resolution(file_b)
    
    resolution = max(resolution_a, resolution_b)
    
    if resolution_a > resolution_b:
        file_a, file_b = file_b, file_a
        resolution_a, resolution_b = resolution_b, resolution_a
        
    factor = resolution_b // resolution_a
    
    points = get_node_points(resolution, number_of_points_per_direction)

    # We do not want to fetch more than 1024 points per direction
    batch_size = 1024

    number_of_batches = (len(points) + batch_size - 1) // batch_size
    
    wasserstein_distance_sum = 0.0
    weights_a = np.ones(resolution) / resolution
    weights_b = np.ones(resolution) / resolution
    
    
    for batch in range(number_of_batches):
        points_in_batch = points[batch * batch_size : (batch+1)*batch_size]
        points_in_batch_downscaled = list(map(lambda point : np.array(point) // factor, points_in_batch))
        data_a = load_points(file_a,
                             points_in_batch_downscaled,
                             resolution, 
                             conserved_variables)
    
        data_b = load_points(file_b,
                             points_in_batch,
                             resolution, 
                             conserved_variables)
        for point_index in range(len(points_in_batch)):
            
            distances = ot.dist(data_a[:,point_index,:],
                                data_b[:,point_index,:], metric='euclidean')
                            
            emd_pairing = wasserstein_inner_compute(weights_a, weights_b, distances)
            wasserstein_distance = np.sum(emd_pairing * distances)
            wasserstein_distance_sum += wasserstein_distance

    return wasserstein_distance_sum / resolution**6
    
def is_power_of_two(n):
    """ see https://stackoverflow.com/a/57027610 """
    return (n != 0) and (n & (n-1) == 0)
    
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="""
Computes the 2 pt wasserstein distance between two files
            """)

    parser.add_argument('--file_a', type=str, required=True,  
                        help='first file')

    parser.add_argument('--file_b', type=str, required=True,  
                        help='second file')

    parser.add_argument('--number_of_points', type=int, default=8,
                        help='Number of points in one direction')
    
    parser.add_argument('--outfile', type=str, required=True,
                        help='Name of output file')

    args = parser.parse_args()
    
    mpi_size = get_global_size()
    
    
    # maybe these two next checks are too strict, but wanted to be on the safe side
    if not is_power_of_two(args.number_of_points):
        raise Exception(f'number_of_points must be power of 2, given {args.number_of_points}')

    if not is_power_of_two(mpi_size):
        raise Exception(f'number of nodes given through MPI must be power of 2, given {mpi_size}')
        
    wasserstein = compute_wasserstein_two_points(args.file_a, args.file_b, args.number_of_points)
    comm = MPI.COMM_WORLD
    sum_distance = comm.reduce(wasserstein, op=MPI.SUM)
    
    if get_rank_global() == 0:
        plot_info.saveData(args.outfile, np.array(sum_distance).reshape(1))
    

"""
Computes the wasserstein distance between two files
"""
import mpi4py
import netCDF4
import ot

# We are not going to plot, but we will save data
import plot_info

def get_rank_global():
    comm = MPI.COMM_WORLD
    return comm.Get_rank()

def get_global_size():
    comm = MPI.COMM_WORLD
    return comm.Get_size()

def get_node_z_range(resolution):
    rank = get_rank_global()
    
    size = get_global_size()

    number_of_planes_per_node = (resolution + size - 1)// size

    start_z = rank * number_of_planes_per_node
    end_z = min(start_z + number_of_planes_per_node, resolution)

    return start_z, end_z

def compute_wasserstein_one_point(file_a, file_b, resolution):
    start_z, end_z = get_node_z_range(resolution)

    
    
if __name__ == '__main__':
    

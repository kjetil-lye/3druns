import numpy as np
import matplotlib

matplotlib.use('Agg')
matplotlib.rcParams['savefig.dpi'] = 600

import matplotlib.pyplot as plt

import sys

sys.path.append('../python')
from plot_info import showAndSave, savePlot, saveData

import netCDF4
import matplotlib2tikz
import os
import h5py
import ot
import sys
import scipy
import scipy.stats
import plot_info

from mpi4py import MPI

import compressible_euler

def load_samples_plane(filename, N, kp, upscale_resolution):
    number_of_variables = len(compressible_euler.conserved_variables)
    data = np.zeros((upscale_resolution, upscale_resolution, N, number_of_variables))
    with netCDF4.Dataset(filename) as f:
        for k in range(N):
            for n, variable_name in enumerate(compressible_euler.conserved_variables):
                d = f.variables[f'sample_{k}_{variable_name}'][kp, :, :]
    
                while d.shape[1] < upscale_resolution:
                    d = np.repeat(np.repeat(d, 2, 0), 2, 1)
    
                data[:, :, k, n] = d

    return data


def load_sample(filename, sample_number, i, j, k):
    sample = np.zeros(len(compressible_euler.conserved_variables))
    with netCDF4.Dataset(filename) as f:
        for n, variable_name in enumerate(compressible_euler.conserved_variables):
            d = f.variables[f'sample_{sample_number}_{variable_name}']
            
            sample[n] = d[i,j,k]

    return sample 


def load_samples(filename, N, i, j, k):
    data = np.zeros((N, len(compressible_euler.conserved_variables)))
    for sample in range(N):
        data[sample, :] = load_sample(filename, sample, i, j, k)
    return data


def wasserstein_point2_fast(a, b, xs, xt):
    """
    Computes the Wasserstein distance for a single point in the spatial domain
    """
    M = ot.dist(xs, xt, metric='euclidean')
    G0 = ot.emd(a, b, M)

    return np.sum(G0 * M)


def get_integration_points(points):
    all_points = []

    for x in points:
        for y in points:
            for z in points:
                all_points.append([x, y, z])

    return all_points


def get_points_per_node(points_base):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    number_of_ranks = comm.Get_size()

    points = get_integration_points(points_base)

    points_per_rank = (len(points) + number_of_ranks - 1) // number_of_ranks

    points_start = rank * points_per_rank

    points_end = min((rank + 1) * points_per_rank, len(points))

    return points[points_start:points_end]


def wasserstein2pt_fast(filename_a, filename_b, N, number_of_integration_points=16):
    """
    Approximate the L^1(W_1) distance (||W_1(nu1, nu2)||_{L^1})
    """

    number_of_variables = len(compressible_euler.conserved_variables)
    a = np.ones(N) / N
    b = np.ones(N) / N
    xs = np.zeros((N, 2 * number_of_variables))
    xt = np.zeros((N, 2 * number_of_variables))
    distance = 0
    if 2**np.log2(number_of_integration_points) != number_of_integration_points:
        raise Exception(f'number_of_integration_points must be a power of 2, given \n{number_of_integration_points}')
    
    points = np.arange(0, number_of_integration_points)
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    for n, (x, y, z) in enumerate(get_points_per_node(points)):
        if rank == 0:
            sys.stdout.write("{}\r".format(n))
            sys.stdout.flush()
        i = int(x * N / number_of_integration_points)
        j = int(y * N / number_of_integration_points)
        k = int(z * N / number_of_integration_points)

        xs[:, :number_of_variables] = load_samples(filename_a, N, i, j, k)
        xt[:, :number_of_variables] = np.repeat(load_samples(filename_b, N // 2, i // 2, j // 2, k // 2), 2, 0)

        for nzp, zp in enumerate(points):
            kp = int(zp * N / number_of_integration_points)
            samples_plane_a = load_samples_plane(filename_a, N, kp, N)
            samples_plane_b = np.repeat(load_samples_plane(filename_b, N // 2, kp // 2, N), 2, 2)

            for nxp, xp in enumerate(points):
                for nyp, yp in enumerate(points):
                    ip = int(xp * N / number_of_integration_points)
                    jp = int(yp * N / number_of_integration_points)

                    xs[:, number_of_variables:] = samples_plane_a[ip, jp, :]

                    xt[:, number_of_variables:] = samples_plane_b[ip, jp, :]

                    distance += wasserstein_point2_fast(a, b, xs, xt)

    distance = comm.allreduce(distance, op=MPI.SUM)
    if rank == 0:
        print()
        print("Done")

    return distance / len(points) ** 6


def plotWassersteinConvergence(name, basename, resolutions, number_of_integration_points):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    wasserstein2pterrors = []
    for r in resolutions[1:]:
        if rank == 0:
            print(r)
        filename = basename.format(resolution=r)
        filename_coarse = basename.format(resolution=r // 2)

        wasserstein2pterrors.append(wasserstein2pt_fast(filename, filename_coarse, r, number_of_integration_points))
        if rank == 0:
            print("wasserstein2pterrors={}".format(wasserstein2pterrors))

    # Only plot from rank 0
    if rank == 0:
        plt.loglog(resolutions[1:], wasserstein2pterrors, '-o', basex=2, basey=2)
        plt.xlabel("Resolution")
        min_value_log = np.floor(np.log2(np.min(wasserstein2pterrors)))
        max_value_log = np.ceil(np.log2(np.max(wasserstein2pterrors)))

        plt.ylim([2 ** min_value_log, 2 ** max_value_log])
        plt.xticks(resolutions[1:], ['${r}^3$'.format(r=r) for r in resolutions[1:]])
        plt.ylabel('$||W_1(\\nu^{2, \\Delta x}, \\nu^{2,\\Delta x/2})||_{L^1(D\\times D)}$')
        plt.title("""Wasserstein convergence for {title}
for second correlation marginal
Using ${number_of_integration_points}^6={total_integration_points}$ equidistant integration points
        """.format(title=name, number_of_integration_points=number_of_integration_points,
                   total_integration_points=number_of_integration_points ** 6))
        showAndSave('%s_wasserstein_convergence_2pt' % name)

        saveData('%s_wasserstein_convergence_2pt_resolutions' % name, resolutions)
        saveData('%s_wasserstein_convergence_2pt_wasserstein' % name, wasserstein2pterrors)


if __name__ == '__main__':
    import sys
    import argparse

    parser = argparse.ArgumentParser(description="""
Computes the wasserstein distances
        """)

    parser.add_argument('--input_basename', type=str, required=True,
                        help='Input filename (should have a format string {resolution})')

    parser.add_argument('--title', type=str, required=True,
                        help='Title of plot')

    parser.add_argument('--number_of_integration_points', type=int, default=10,
                        help='Number  of integration points')

    args = parser.parse_args()

    basename = args.input_basename
    name = args.title
    number_of_integration_points = args.number_of_integration_points

    plot_info.add_additional_plot_parameters("basename", basename)
    plot_info.add_additional_plot_parameters("number_of_integration_points", number_of_integration_points)

    resolutions = [64, 128, 256, 512]
    plotWassersteinConvergence(name, basename, resolutions, number_of_integration_points)

#!/bin/bash
set -e

# Remember that you need to download the Richtmeyer-Meshkov data from daint
for resolution in 64 128 256; do 
    if [[ ! -f $SCRATCH/rm/N${resolution}/rm_cuda_0.nc ]]
    then
	echo "Missing file: $SCRATCH/rm/N${resolution}/rm_cuda_0.nc"
	echo "Copy it from daint (or other data source)"
    fi
done

for resolution in 64 128 256; do 
    multi_z=${resolution}; 
    multi_y=$((1024/$resolution)); 
    total=$((${multi_z}*$multi_y));
    
    bsub -n $total -W 24:00 -N -B -R 'rusage[mem=1000]' mpirun -np ${total} python ../python/compute_single_pair_wasserstein.py --file_a $SCRATCH/rm/N${resolution}/rm_cuda_0.nc --file_b $SCRATCH/rm/N512/rm_cuda_0.nc --multi_y ${multi_y} --multi_z ${multi_z} --outfile wasserstein_one_point_rm_0_1_reference_${resolution}
done

for resolution in 64 128 256; do 
    total=512
    
    bsub -n $total -W 24:00 -N -B -R 'rusage[mem=1000]' mpirun -np ${total} python ../python/compute_single_pair_wasserstein_two_points.py --file_a $SCRATCH/rm/N${resolution}/rm_cuda_0.nc --file_b $SCRATCH/rm/N512/rm_cuda_0.nc --number_of_points 16 --outfile wasserstein_two_points_rm_0_1_reference_${resolution}
done


for statistics in "single_sample" "mean" "variance";
do
    total=1     
    bsub -n $total -W 24:00 -N -B -R 'rusage[mem=1000]' python ../python/compute_convergence.py --input_basename $SCRATCH/rm/N{resolution}/rm_cuda_0.nc --statistic_name ${statistics} \
	--title "Richtmeyer-Meshkov $\\epsilon=0.1$" --reference
done



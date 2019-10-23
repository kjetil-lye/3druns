#!/bin/bash
set -e

## NOTE! We could not fit all datasets at the same time on euler, 
## Therfore, we copied one dataset (one Hurst index H) from daint to euler,
## computed the wasserstein distance, then deleting the dataset on euler, 
## and copy the next one

function submit { 
    bsub -W 120:00 -R 'rusage[mem=32000]' "$@"
}



H=$1

input_filename=/cluster/project/sam/klye/H${H//./_}/N{resolution}/fbm_1.nc

# Check that we have all the files
for resolution in 64 128 256 512
do
    filename_at_resolution=${input_filename//'{resolution}'/${resolution}}
    if [[ ! -f "${filename_at_resolution}" ]]
    then
	echo "Missing file: ${filename_at_resolution}"
	exit 1
    fi
done
submit python ../python/compute_wasserstein.py \
    --input_basename=${input_filename} \
    --starting_resolution 64 \
    --title "Fractional Brownian motion \$H=${H}, T=0.2\$"  \
    --reference_solution


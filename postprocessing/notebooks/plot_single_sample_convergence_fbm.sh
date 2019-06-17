#!/bin/bash
for var in mx my mz E rho; do 
    for H in 0_05 0_1 0_5 0_75; do 
	python ../python/compute_single_sample_congvergence_large.py --input $SCRATCH/3druns/fbm/single/H${H}/N{resolution}/fbm_1.nc --title "Fractional Brownian motion \$H=${H//_/.}, T=0.2\$" --starting_resolution 32 --variable ${var}; 
    done; 
done

for var in mx my mz E rho; do 
    for H in 0_05 0_1 0_5 0_75; do 
	python ../python/compute_single_sample_congvergence_large.py --input $SCRATCH/3druns/fbm/single/H${H}/N{resolution}/fbm_0.nc --title "Fractional Brownian motion \$H=${H//_/.}, T=0\$" --starting_resolution 32 --variable ${var}; 
    done; 
done

#!/bin/bash
for stat in mean variance; 
do 
    for var in mx my mz E rho; 
    do 
	for H in 0_1 0_5 0_75; 
	do 
	    python ../python/compute_mean_variance_convergence.py \
		   --input_basename_a $SCRATCH/3druns/fbm/stats/H${H}/N{resolution}/fbm_{stat}_1.nc \
		   --name_a "double"\
		   --input_basename_b $SCRATCH/3druns/fbm/stats_float/H${H}/N{resolution}/fbm_{stat}_0.nc \
		   --name_b "float"\
		   --title "Fractional Brownian motion \$H=${H//_/.}, T=0.2\$" --starting_resolution 32 \
		   --stat ${stat}\
		   --variable ${var}\
		   --not_zoom \
		   --compute_rate; 
	done; 
    done; 
done


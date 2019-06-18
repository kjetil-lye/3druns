#!/bin/bash
for stat in mean variance; 
do 
    for var in mx my mz E rho; 
    do 
	for H in 0_5; 
	do 
	    python ../python/compute_mean_variance_convergence.py --input $SCRATCH/3druns/fbm/stats/H${H}/N{resolution}/fbm_{stat}_1.nc --title "Fractional Brownian motion \$H=${H//_/.}, T=0.2\$" --starting_resolution 32 --stat ${stat} --variable ${var} --not_zoom --compute_rate; 
	done; 
    done; 
done


for stat in mean variance; 
do 
    for var in mx my mz E rho; 
    do 
	for H in 0_5; 
	do 
	    python ../python/compute_mean_variance_convergence.py --input $SCRATCH/3druns/fbm/stats/H${H}/N{resolution}/fbm_{stat}_0.nc --title "Fractional Brownian motion \$H=${H//_/.}, T=0.0\$" --starting_resolution 32 --stat ${stat} --variable ${var} --not_zoom --compute_rate; 
	done; 
    done; 
done

#!/bin/bash
for stat in mean variance; 
do 
    for var in all mx my mz E rho; 
    do 
	for H in 0_05
	do 
	    python ../python/compute_mean_variance_convergence.py --input_basename $SCRATCH/3druns/richtmeyermeshkov/short_time/p${H}/N{resolution}/richtmeyermeshkov_{stat}_0.nc --title "Richtmeyer-Meshkov instability \$\\epsilon=${H//_/.}, T=2\$" --starting_resolution 64 --stat ${stat} --variable ${var} --compute_rate --reference_solution --not_zoom; 
	done; 
    done; 
done


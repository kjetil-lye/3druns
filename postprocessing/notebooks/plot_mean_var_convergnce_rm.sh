#!/bin/bash
for stat in mean variance; 
do 
    for var in mx my mz E rho; 
    do 
	for H in 0_05
	do 
	    python ../python/compute_mean_variance_convergence.py --input_basename $SCRATCH/3druns/richtmeyermeshkov/stats/p${H}/N{resolution}/rm_cuda_{stat}_0.nc --title "Richtmeyer-Meshkov \$\\epsilon=${H//_/.}, T=4\$" --starting_resolution 64 --stat ${stat} --variable ${var} --not_zoom --compute_rate; 
	done; 
    done; 
done

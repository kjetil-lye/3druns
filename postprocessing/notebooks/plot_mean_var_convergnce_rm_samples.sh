#!/bin/bash
for stat in mean variance; 
do 
    for var in mx my mz E rho; 
    do 
	for H in 0_05
	do 
	    python ../python/compute_mean_variance_convergence.py --input_basename $SCRATCH/3druns/richtmeyermeshkov/stats/p${H}/N{resolution}/richtmeyermeshkov_samples_{stat}_0.nc --title "Richtmeyer-Meshkov instability \$\\epsilon=${H//_/.}, T=4\$ (using $M=N$ samples)" --starting_resolution 64 --stat ${stat} --variable ${var} --compute_rate; 
	done; 
    done; 
done


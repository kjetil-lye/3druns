#!/bin/bash
for stat in mean variance; 
do 
    for var in all mx my mz E rho; 
    do 
	for H in 0_05
	do 
	    python ../python/compute_mean_variance_convergence.py --input_basename /project/s913/klye/3druns_fbm/3druns/richtmeyermeshkov/stats/p${H}/N{resolution}/richtmeyermeshkov_{stat}_0.nc --title "Richtmeyer-Meshkov instability \$\\epsilon=${H//_/.}, T=4\$" --starting_resolution 64 --stat ${stat} --variable ${var} --compute_rate --not_zoom --reference_solution; 
	done; 
    done; 
done


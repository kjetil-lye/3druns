#!/bin/bash
for stat in mean variance; 
do 
    for var in all mx my mz E rho; 
    do 
	for H in 0_01 0_1
	do 
	    python ../python/compute_mean_variance_convergence.py --input_basename $SCRATCH/3druns_new/kelvinhelmholtz_3d_tube/stats/p${H}/N{resolution}/kh_{stat}_0.nc --title "Kelvin-Helmholtz \$\\epsilon=${H//_/.}, T=2\$" --starting_resolution 64 --stat ${stat} --variable ${var} --compute_rate --reference_solution --not_zoom; 
	done; 
    done; 
done


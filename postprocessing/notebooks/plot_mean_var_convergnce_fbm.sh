#!/bin/bash
for stat in mean variance; 
do 
    for var in all mx my mz E rho; 
    do 
	for H in 0_1 0_5 0_75; 
	do 
	    python ../python/compute_mean_variance_convergence.py --input_basename  /project/s913/klye/3druns_fbm/3druns/fbm/stats/H${H}/N{resolution}/fbm_{stat}_1.nc --title "Fractional Brownian motion \$H=${H//_/.}, T=0.2\$" --starting_resolution 32 --stat ${stat} --variable ${var} --not_zoom --compute_rate --reference_solution; 
	done; 
    done; 
done


for stat in mean variance; 
do 
    for var in all mx my mz E rho; 
    do 
	for H in 0_1 0_5 0_75; 
	do 


	    python ../python/compute_mean_variance_convergence.py --input_basename  /project/s913/klye/3druns_fbm/3druns/fbm/stats/H${H}/N{resolution}/fbm_{stat}_0.nc --title "Fractional Brownian motion \$H=${H//_/.}, T=0.0\$" --starting_resolution 32 --stat ${stat} --variable ${var} --not_zoom --compute_rate --reference_solution; 
	done; 
    done; 
done

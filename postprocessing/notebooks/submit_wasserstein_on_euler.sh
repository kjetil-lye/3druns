#!/bin/bash
N=50

for int_points in 10 20 40;
do
    
    for t in 0 1;
    do

	for p in 0.1 0.01;
	do
	    bsub -n $N -R "rusage[mem=8000]" mpirun -np 50 python ../python/wasserstein_two_point.py --input_basename "/cluster/project/sam/klye/3druns_kh_tube/kelvinhelmholtz_3d_tube/stats/kelvinhelmholtz_{resolution}_${p}/kh_${t}.nc" --title "Kelvin-Helmholtz \$T=$((2*${t}))\$ \$\\epsilon=$p\$ \$K_I=${int_points}\$"
	    
	done
    done
done



#!/bin/bash
N=50

for int_points in 8 16 32 64
do
    
    for t in 0 1;
    do

	for p in 0.1;
	do
	    bsub -W 48:00 -n $N -R "rusage[mem=8000]" mpirun -np 50 python \
		 ../python/wasserstein_two_point.py \
		 --input_basename \
		 "/cluster/project/sam/klye/3druns_kh_tube/kelvinhelmholtz_3d_tube/stats/kelvinhelmholtz_{resolution}_${p}/kh_${t}.nc" \
		 --title "Kelvin-Helmholtz \$T=$((2*${t}))\$ \$\\epsilon=$p\$ \$K_I=${int_points}\$"\
		 --number_of_integration_points=${int_points}
	    
	done
    done
done

for t in 0 1;
do

    for p in 0.1 0.01;
    do
	bsub -W 24:00 -R "rusage[mem=8000]" python \
	     ../python/compute_wasserstein.py \
	    --input_basename "/cluster/project/sam/klye/3druns_kh_tube/kelvinhelmholtz_3d_tube/stats/kelvinhelmholtz_{resolution}_${p}/kh_${t}.nc" \
	    --title "Kelvin-Helmholtz \$T=$((2*${t}))\$ \$\\epsilon=$p\$ \$K_I=${int_points}\$"
    done
done




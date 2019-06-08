#!/bin/bash
set -e
export OMP_NUM_THREADS=1
for t in 1;
do
    for x in 64 128 256 512; 
    do
	for pert in 0.1;
	do

	    cd kh_N${x}_${pert}
	    for p in 1 2 3;
	    do


		bsub -W 120:00 -n 8 -R "rusage[ngpus_excl_p=8,mem=8000] span[ptile=8]" -N -B   mpirun -np 8 ../../build/structure_functions -i /cluster/work/math/klye/3druns_kh_tube/kelvinhelmholtz_3d_tube/stats/kelvinhelmholtz_${x}_${pert}/kh_${t}.nc -o structure_cuda_t_${t}_p_${p} --samples ${x} --number-of-h  $(( ($x*32)/1024 )) --nx $x --ny $x --nz $x --platform cuda
	    done
	cd ..;
	done
    done
done

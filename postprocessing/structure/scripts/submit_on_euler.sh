#!/bin/bash
set -e
for r in 64 128 256 512; 
do
    for p in 0.1 0.01;
    do
	cd kh_N${x}_${p}
	

	bsub ../../build/structure_functions -i /cluster/project/sam/klye/3druns_kh_tube/kelvinhelmholtz_3d_tube/stats/kelvinhelmholtz_${x}_${p}/kh_1.nc -o structure --samples ${x} --equation euler3 --number-of-h $(( ($x*32)/1024 )) --nx $x --ny $x --nz $x;
	cd ..;
    done
done

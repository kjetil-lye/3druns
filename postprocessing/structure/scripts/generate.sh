#!/bin/bash
set -e
#srun ../../../build/structure_functions -i INFILE -o OUTFILE --samples SAMPLES --equation euler3 --number-of-h NUMBEROFH --nx NX --ny NX --nz NX

for nx in 64 128 256 512;
do
    for pert in 0.1 0.01;
    do
	mkdir kh_N${nx}_${pert};
	cd kh_N${nx}_${pert};
	cp ../submit.sh ./
	sed -i "s/INFILE/kelvinhelmholtz_3d_tube\/stats\/kelvinhelmholtz_${nx}_${pert}\/kh_1.nc/g" submit.sh
	sed -i "s/OUTFILE/kh_structure/g" submit.sh
	sed -i "s/SAMPLES/${nx}/g" submit.sh
	NUMBEROFH=$((($nx*32)/1024))
	sed -i "s/NUMBEROFH/${NUMBEROFH}/g" submit.sh
	sed -i "s/NX/${nx}/g" submit.sh
	cd ..;
    done
done

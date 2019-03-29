#!/bin/bash
set -e

PERTURBATION=0.01
SAMPLES=512
for r in 32 64 128 256 512;
do
    NH=$(($r/32))
    name=kelvinhelmholtz_${r}_${PERTURBATION}
    mkdir ${name}
    cp template/kelvinhelmholtz.* ./${name}/
    sed -i "s/NX/${r}/g" ./${name}/kelvinhelmholtz.xml
    sed -i "s/NH/${NH}/g" ./${name}/kelvinhelmholtz.xml
    sed -i "s/SAMPLES/${SAMPLES}/g" ./${name}/kelvinhelmholtz.xml
    sed -i "s/PERTURBATION/${PERTURBATION}/g" ./${name}/kelvinhelmholtz.py
done
    
    

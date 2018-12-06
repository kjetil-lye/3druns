#!/bin/bash
set -e

PERTURBATION=0.1
SAMPLES=1
for r in 32 64 128 256 512;
do
    name=kelvinhelholtz_${r}_${PERTURBATION}
    mkdir ${name}
    cp ../template/kelvinhelmholtz.* ./${name}/
    sed -i "s/NX/${r}/g" ./${name}/kelvinhelmholtz.xml
    sed -i "s/SAMPLES/${SAMPLES}/g" ./${name}/kelvinhelmholtz.xml
    sed -i "s/PERTURBATION/${PERTURBATION}/g" ./${name}/kelvinhelmholtz.py
done
    
    

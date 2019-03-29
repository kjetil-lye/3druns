#!/bin/bash

set -e
for r in 64 128 256 512 1024;
do
    NH=$((($r*32)/1024));
    mkdir N${r}
    cd N${r}
    cp ../brownian_base/brownian.* ./
    cp ../submit.sh ./
    sed -i "s/NX/${r}/g" brownian.xml;
    sed -i "s/NH/${NH}/g" brownian.xml;

    sed -i "s/NX/${r}/g" submit.sh;
    parameters=$((3*$r*$r*$r))
    sed -i "s/PARAMETERS/${parameters}/g" brownian.xml
    NODES=1
    NODES_X=1
    NODES_Y=1
    NODES_Z=1
    NODES_SAMPLE=1

    if [[ "$r" -eq "512" ]];
    then
	NODES=8
	NODES_X=2
	NODES_Y=2
	NODES_Z=2
	NODES_SAMPLE=1
    fi;

    if [[ "$r" -eq "1024" ]];
    then
	NODES=64
	NODES_X=4
	NODES_Y=4
	NODES_Z=4
	NODES_SAMPLE=1
    fi;	

    sed -i "s/NODES_TOTAL/${NODES}/g" submit.sh;
    sed -i "s/NODES_X/${NODES_X}/g" submit.sh;
    sed -i "s/NODES_Y/${NODES_Y}/g" submit.sh;
    sed -i "s/NODES_Z/${NODES_Z}/g" submit.sh;
    sed -i "s/NODES_SAMPLE/${NODES_SAMPLE}/g" submit.sh;
    cd ..;
done

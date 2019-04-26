#!/bin/bash

set -e

for r in 64 128 256 512;
do
    NH=$((($r*32)/1024));
    mkdir N${r}
    cd N${r}
    cp ../cloudshock_base/cloudshock.* ./
    cp ../submit.sh ./
    sed -i "s/NX/${r}/g" cloudshock.xml;
    sed -i "s/NH/${NH}/g" cloudshock.xml;

    sed -i "s/NX/${r}/g" submit.sh;

    NODES=128
    NODES_X=1
    NODES_Y=1
    NODES_Z=1
    NODES_SAMPLE=128

    if [[ "$r" -eq "512" ]];
    then
	NODES=1024
	NODES_X=2
	NODES_Y=2
	NODES_Z=2
	NODES_SAMPLE=128
    fi;	
    sed -i "s/NODES_TOTAL/${NODES}/g" submit.sh;
    sed -i "s/NODES_X/${NODES_X}/g" submit.sh;
    sed -i "s/NODES_Y/${NODES_Y}/g" submit.sh;
    sed -i "s/NODES_Z/${NODES_Z}/g" submit.sh;
    sed -i "s/NODES_SAMPLE/${NODES_SAMPLE}/g" submit.sh;
    cd ..;
done

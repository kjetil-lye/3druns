#!/bin/bash

for s in `seq 0 $((1024/16))`; 
do 
    sample_start=$((16*$s)); 
    sample_end=$((16*($s+1))); 
    mkdir sample_${sample_start}; 
    cp taylorgreen.py sample_${sample_start}/; 
    cp taylorgreen_base.xml sample_${sample_start}/taylorgreen.xml; 
    sed -i "s/START/${sample_start}/g" sample_${sample_start}/taylorgreen.xml; 
done

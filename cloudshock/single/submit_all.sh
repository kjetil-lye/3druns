#!/bin/bash

set -e

for r in 64 128 256 512 1024;
do
    cd N${r}
    if [ $r -lt 256 ] ;
	then 
	N=1
     else
	N=$(($r/(128)))
     fi
    echo $N


    bsub -N -B -W 24:00 -n $N -R "rusage[ngpus_excl_p=8,mem=8000]" mpirun -np $N ~/alsvinn/build/alsuqcli/alsuqcli --multi-z $N cloudshock.xml
    cd ..
done

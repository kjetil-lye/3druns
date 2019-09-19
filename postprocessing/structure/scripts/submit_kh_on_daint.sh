#!/bin/bash
set -e
if [ -z "${STRUCTURE_BIN_DIR}" ]
then
    echo "STRUCTURE_BIN_DIR needs to be exported to a folder containint structure_standalone"
    exit 1
fi

if [ ! -f "${STRUCTURE_BIN_DIR}/structure_standalone" ]
then
    echo "STRUCTURE_BIN_DIR does not contain structure_standalone"
    exit 1
fi


export OMP_NUM_THREADS=1
for t in 0;
do
    for x in 64 128 256 512; 
    do
	for pert in 0.1 0.01
	do

	    folder="kh_new_pert/p${pert//./_}/N${x}"
	    mkdir -p ${folder}

	    for p in 1 2 3;
	    do
		if [ $x -gt 256 ];
		then
		    NODES=16
		else
		    NODES=1
		fi
		

		python -m submit_command_on_daint \
		       -w ${folder} \
		       --nodes ${NODES} \
		       --name "kh_${t}_${pert}_${x}_${p}" \
		       --command "$STRUCTURE_BIN_DIR/structure_standalone -i $SCRATCH/3druns_new/kelvinhelmholtz_3d_tube/stats/p${pert//./_}/N${x}/kh_${t}.nc -o structure_kh_cuda_t_${t}_p_${p} --samples ${x} --number-of-h  16 --nx 512 --ny 512 --nz 512 --platform cuda --p ${p}" \
		       "$@"
	    done
	done
    done
done

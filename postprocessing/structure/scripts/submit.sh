#!/bin/bash -l
#SBATCH --job-name=postprocess
#SBATCH --mail-type=ALL
#SBATCH --mail-user=kjetil.lye@sam.math.ethz.ch
#SBATCH --time=24:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-core=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --partition=normal
#SBATCH --constraint=gpu
#SBATCH --account=s913

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
srun ../../build/structure_functions -i ${THREEDIMS_PATH}/INFILE -o OUTFILE --samples SAMPLES --equation euler3 --number-of-h NUMBEROFH --nx NX --ny NX --nz NX

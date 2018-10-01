#!/bin/bash -l
#SBATCH --job-name=copydata
#SBATCH --mail-type=ALL
#SBATCH --mail-user=kjetil.lye@sam.math.ethz.ch
#SBATCH --time=24:00:00
#SBATCH --partition=xfer

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

module unload xalt
srun rsync -av $1 $2
if [ -n '$3' ]; then
    sbatch --dependency=afterok:$SLURM_JOB_ID $3
fi

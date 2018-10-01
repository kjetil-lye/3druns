#!/bin/bash -l
#SBATCH --job-name=testtime
#SBATCH --mail-type=ALL
#SBATCH --mail-user=kjetil.lye@sam.math.ethz.ch
#SBATCH --time=24:00:00
#SBATCH --nodes=1024
#SBATCH --ntasks-per-core=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --partition=normal
#SBATCH --constraint=gpu
#SBATCH --account=s839

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

srun shifter run --mpi kjetilly/alsvinn:git alsuqcli --multi-sample 64 --multi-z 16 taylorgreen.xml
 

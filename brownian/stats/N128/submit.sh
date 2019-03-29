#!/bin/bash -l
#SBATCH --job-name=brownian
#SBATCH --mail-type=ALL
#SBATCH --mail-user=kjetil.lye@sam.math.ethz.ch
#SBATCH --time=24:00:00
#SBATCH --nodes=128
#SBATCH --ntasks-per-core=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --partition=normal
#SBATCH --constraint=gpu

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
srun  $HOME/alsvinn/build_float/alsuqcli/alsuqcli --multi-z 1 --multi-x 1 --multi-y 1 --multi-sample 128 brownian.xml

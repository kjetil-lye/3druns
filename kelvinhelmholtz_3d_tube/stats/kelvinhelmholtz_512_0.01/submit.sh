#!/bin/bash -l
#SBATCH --job-name=kelvinhelmholtz_512
#SBATCH --mail-type=ALL
#SBATCH --mail-user=kjetil.lye@sam.math.ethz.ch
#SBATCH --time=24:00:00
#SBATCH --nodes=1024
#SBATCH --ntasks-per-core=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --partition=normal
#SBATCH --constraint=gpu

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
srun  $HOME/alsvinn/build_float/alsuqcli/alsuqcli --multi-z 2 --multi-x 2 --multi-y 2 --multi-sample 128 kelvinhelmholtz.xml

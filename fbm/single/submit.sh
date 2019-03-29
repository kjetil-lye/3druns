#!/bin/bash -l
#SBATCH --job-name=fbm_HURST_NX
#SBATCH --mail-type=ALL
#SBATCH --mail-user=kjetil.lye@sam.math.ethz.ch
#SBATCH --time=24:00:00
#SBATCH --nodes=NODES_TOTAL
#SBATCH --ntasks-per-core=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --partition=normal
#SBATCH --constraint=gpu

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
srun  $HOME/alsvinn/build/alsuqcli/alsuqcli --multi-z NODES_X --multi-x NODES_Y --multi-y NODES_Z --multi-sample NODES_SAMPLE cloudshock.xml

#!/bin/bash -l
#SBATCH --job-name="job_name"
#SBATCH --time=24:00:00
#SBATCH --nodes=64
#SBATCH --ntasks-per-core=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --partition=normal
#SBATCH --constraint=gpu
#SBATCH --account=s913

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
export CRAY_CUDA_MPS=1

srun $HOME/alsvinn/build/alsuqcli/alsuqcli --multi-x 4 --multi-y 4 --multi-z 4 kelvinhelmholtz.xml

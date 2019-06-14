#!/bin/bash -l
#SBATCH --job-name="job_name"
#SBATCH --time=24:00:00
#SBATCH --nodes=NODES
#SBATCH --ntasks-per-core=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --partition=normal
#SBATCH --constraint=gpu
#SBATCH --account=s913

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
export CRAY_CUDA_MPS=1

srun $HOME/alsvinn/build/alsuqcli/alsuqcli --multi-x NX --multi-y NX --multi-z NX kelvinhelmholtz.xml

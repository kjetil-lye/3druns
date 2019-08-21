#!/bin/bash
set -e

python ../../tools/submit_command_on_daint.py --name rm_wasser --command "python ../python/compute_wasserstein.py --input_basename $SCRATCH/3druns/richtmeyermeshkov/stats/p0_05/N{resolution}/rm_cuda_0.nc --starting_resolution 64 --title 'Richtmeyer-Meshkov \$\\epsilon=0.05, T=4\$'"

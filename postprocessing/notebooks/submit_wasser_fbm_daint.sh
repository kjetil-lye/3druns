#!/bin/bash

for H in 0.1 0.5 0.75;
do
    python ../../tools/submit_command_on_daint.py --command "python ../python/compute_wasserstein.py --input_basename $SCRATCH/3druns/fbm/stats/H${H//./_}/N{resolution}/fbm_1.nc --starting_resolution 64 --title 'Fractional Brownian motion \$H=${H}, T=0.2\$'"  --name wasserstein_fbm${H//./}
done

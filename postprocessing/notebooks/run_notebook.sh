#!/bin/bash
set -e
if [ -z "$THREEDIMS_PATH" ]
then
    echo "Missing THREEDIMS_PATH from ENV"
    echo "Set it using"
    echo "    export THREEDIMS_PATH=<path to folder containing the 3druns repository WITH DATA FILES>"
    exit 1
fi


$HOME/.local/bin/jupyter nbconvert --ExecutePreprocessor.timeout=-1 --to notebook --execute kelvin_helmholtz.ipynb --output kelvin_helmholtz_output.ipynb

$HOME/.local/bin/jupyter nbconvert --ExecutePreprocessor.timeout=-1 --to notebook --execute cloudshock.ipynb --output cloudshock_output.ipynb


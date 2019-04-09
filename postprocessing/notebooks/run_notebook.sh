#!/bin/bash
set -e
if [ -z "$3DRUNS_KH_PATH" ]
then
    echo "Missing 3DRUNS_PATH from ENV"
    echo "Set it using"
    echo "    export 3DRUNS_PATH=<path to folder containing the 3druns repository WITH DATA FILES>"
    exit 1
fi


$HOME/.local/bin/jupyter nbconvert --ExecutePreprocessor.timeout=-1 --to notebook --execute kelvin_helmholtz.ipynb --output kelvin_helmholtz_output.ipynb


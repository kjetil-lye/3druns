#!/bin/bash

set -e
output_base_folder=/cluster/project/sam/klye/
output_folder=${output_base_folder}/kh_fixed_perturbation
if [[ -f ${output_folder} ]]
then
    if [[ "$1" != "repeat" ]]
    then
	echo "${output_folder} exists!"
	echo "Either move it, or rerun with the 'repeat' option"
	exit 1
    fi
fi

rsync -rltP -e ssh klye@ela.cscs.ch:/project/s913/klye/kelvinhelmholtz_3d_tube_fixed_perturbation/ ${output_base_folder}

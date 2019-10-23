#!/bin/bash

set -e
H=$1
output_base_folder=/cluster/project/sam/klye/
output_folder=${output_base_folder}/${H//./_}
if [[ -f ${output_folder} ]]
then
    if [[ "$2" != "repeat" ]]
    then
	echo "${output_folder} exists!"
	echo "Either move it, or rerun with the 'repeat' option"
	exit 1
    fi
fi

rsync -rltP -e ssh klye@ela.cscs.ch:/project/s913/klye/3druns_fbm/3druns/fbm/stats/H${H//./_} ${output_base_folder}

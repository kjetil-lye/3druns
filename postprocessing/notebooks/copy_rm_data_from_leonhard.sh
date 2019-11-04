#!/bin/bash

set -e
output_base_folder=/cluster/project/sam/klye/
output_folder=${output_base_folder}/rm
if [[ -f ${output_folder} ]]
then
    if [[ "$1" != "repeat" ]]
    then
	echo "${output_folder} exists!"
	echo "Either move it, or rerun with the 'repeat' option"
	exit 1
    fi
fi

rsync -rltP -e ssh klye@login.leonhard.ethz.ch:/cluster/work/math/klye/3druns_richtmeyer ${output_base_folder}

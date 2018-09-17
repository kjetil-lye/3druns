#!/bin/bash
folder=$(dirname $1)
mkdir ${folder//"$2"/}/
cp -r $1 ${1//"$2"/}

#!/bin/bash

set -e

for r in 64 128 256 512 1024;
do
    mkdir N${r}
    cd N${r}
    cp ../cloudshock_base/cloudshock.* ./
    sed -i "s/NX/${r}/g" cloudshock.xml;
    cd ..;
done

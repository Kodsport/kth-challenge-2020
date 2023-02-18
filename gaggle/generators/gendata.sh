#!/bin/bash

cd $(dirname $0)

SOL=../submissions/accepted/per
make $SOL "CXXFLAGS=-g -O2 -std=gnu++17 -static"
mkdir -p ../data/secret

python gendata.py
for f in ../data/secret/*.in; do
    echo $f
    time $SOL < $f > ${f%.in}.ans
done

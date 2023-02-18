#!/bin/bash

for f in */*.in; do
    if [ -f ${f%.in}.png ]; then
        continue
    fi
    echo $f
    cat $f ${f%.in}.ans | timeout 5m asy -f png visualize.asy -o ${f%.in}.png;
done

#!/bin/bash

name=$1
dt=`date "+%Y%m%d"`
dirName=${dt}_${name}

pyInitSrc=`cat <<'EOF'
import math

i = int(input())
n, m = map(int, input().split(" "))
li = list(map(int, input().split(" ")))
EOF
`

mkdir $dirName
cd $dirName

for q in a b c d e f
do
    touch ./${q}.py
    echo "$pyInitSrc" > ./${q}.py
done
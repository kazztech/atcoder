#!/bin/bash

name=$1
dt=`date "+%Y%m%d"`
dirName=${dt}_${name}

mkdir $dirName
cd $dirName

pyContent=`cat <<'EOF'
import math

i = int(input())
n, m = map(int, input().split(" "))
li = list(map(int, input().split(" ")))
EOF
`

for q in a b c d e f
do
    touch ./${q}.py
    echo "$pyContent" > ./${q}.py
done
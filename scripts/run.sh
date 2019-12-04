#!/bin/sh


if [ -z $1 ]; then
  path="cases/case1.json"
else
  path=$1
fi

python3 main.py $path

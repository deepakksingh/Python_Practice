#!/bin/sh

count=0
numOfTimes=5
echo "EXPERIMENT: number of iterations: $numOfTimes"
while [ $count -lt $numOfTimes ]
do
  #training
  python file.1py

  #validation
  python file2.py
    
  count=`expr $count + 1`
done
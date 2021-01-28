#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    Sums=[]
    for i in range(len(arr)-2):
        for ii in range(len(arr[i])-2):
            HGSum = 0
            HGSum = HGSum+ arr[i][ii]   + arr[i][ii+1]   + arr[i][ii+2]
            HGSum = HGSum+                arr[i+1][ii+1]
            HGSum = HGSum+ arr[i+2][ii] + arr[i+2][ii+1] + arr[i+2][ii+2]
            Sums.append(HGSum)
            
    return max(Sums)
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
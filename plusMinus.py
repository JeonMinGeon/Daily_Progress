#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positive_num = 0
    negative_num = 0
    zero_num = 0
    length = len(arr)
    for i in arr:
        if i>0:
            positive_num += 1
        elif i<0:
            negative_num += 1
        else: 
            zero_num += 1
    print('{:.6f}'.format(positive_num/length))
    print('{:.6f}'.format(negative_num/length))
    print('{:.6f}'.format(zero_num/length))
    
    
    
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

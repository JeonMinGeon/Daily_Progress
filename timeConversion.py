#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    conv_s = s
    if s[-2:] == "PM":
        if s[:2] == "12":
            return s[:-2]
        else:
            conv_s = str(12+int(str(s[:2])))+s[2:]
    if s[-2:] == "AM":
        if s[:2] == "12":
            conv_s = "00"+s[2:]
        else:
            return s[:-2]
    
    return conv_s[:-2]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)
    print(result)
    f.write(result + '\n')

    f.close()

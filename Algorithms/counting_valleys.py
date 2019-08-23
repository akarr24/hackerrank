# -*- coding: utf-8 -*-
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    s = list(s)
    step = 0
    v = 0
    for item in range(0,n):
        if s[item] == 'U':
            step += 1
        elif s[item] == 'D':
            step -= 1
        
        if step == 0 and s[item] == 'U':
            v += 1
    
    return v

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()


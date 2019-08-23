# -*- coding: utf-8 -*-
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    h_break = 0
    w_break = 0
    max = scores[0]
    min = scores[0]
    for i in range(1, len(scores)):
        if scores[i] > max:
            max = scores[i]
            h_break += 1
        if scores[i] < min:
            min = scores[i]
            w_break += 1
    
    return h_break, w_break


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()



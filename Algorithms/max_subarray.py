#!/bin/python3

import math
import os
import random
import re
import sys
#maxSubarray
# Complete the maxSubarray function below.
def maxSubarray(arr):
    #Largest subsequence value
    global_max = current_max = arr[0]
    for i in range(1, len(arr)):
        current_max = max(arr[i], current_max + arr[i])
        global_max = max(global_max, current_max)
    # For max non-continuous sub array, order doesn't matter
    arr.sort()
    sum = 0
    if(arr[ len(arr) - 1 ] <= 0):
        sum = arr[len(arr) - 1]
    else:  
        for item in arr:
            if item > 0:
                sum += item

    return global_max, sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

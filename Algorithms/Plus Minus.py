#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    n = len(arr)
    a1 = len([x for x in arr if x > 0]) / n
    a2 = len([x for x in arr if x == 0]) / n
    a3 = len([x for x in arr if x < 0]) / n

    
    print('%.6f'%a1)
    print('%.6f'%a3)
    print('%.6f'%a2)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

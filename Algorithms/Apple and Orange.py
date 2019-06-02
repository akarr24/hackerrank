#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_new = [x+a for x in apples]
    oranges_new = [x+b for x in oranges]
    #print(apples_new)
    #print(oranges_new)
    apples_new = [x for x in apples_new  if x >= s if x <= t]
    #print(apples_new)
    oranges_new = [x for x in oranges_new if x >= s if x <= t]

    print(len(apples_new))
    print(len(oranges_new))


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)

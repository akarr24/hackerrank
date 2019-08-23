# -*- coding: utf-8 -*-
#!/bin/python3

import os
import sys

def pageCount(n, p):
   total = n//2
   right = p//2
   left = total - right
   return min(right, left)

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()



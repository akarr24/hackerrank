# -*- coding: utf-8 -*-
import math
import os
import random
import re
import sys

def shift_left(d,l):
    d = d % len(l)
    head = l[:d]
    l[:d] = []
    l.extend(head)
    return l

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    l = shift_left(d,a)

    for item in l:
        print(item, end = " ")

# -*- coding: utf-8 -*-
#!/bin/python3

import sys

input()
count = [0]*6
for t in map(int,input().strip().split()):
    count[t] += 1
print(count.index(max(count)))




#array_manipulation
# -*- coding: utf-8 -*-

n, inputs = [int(n) for n in input().split(" ")]
l = [0 for _ in range(0, n+1)]
for _ in range(inputs):
    x, y, incr = [int(n) for n in input().split(" ")]
    l[x-1] += incr
    if((y)<=len(l)): 
        l[y] -= incr
max = x = 0
for i in l:
   x=x+i;
   if(max<x): 
       max=x
print(max)


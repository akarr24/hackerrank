# -*- coding: utf-8 -*-
#!/bin/python3

import sys

def solve(year):
    # Complete this function
     if (year == 1918):
        return '26.09.1918'
     elif ((year <= 1917) and (year%4 == 0)) or ((year > 1918) and (year%400 == 0 or     (year%4== 0) and (year%100 != 0))):
        return '12.09.%s' %year
     else:
        return '13.09.%s' %year

year = int(input().strip())
result = solve(year)
print(result)

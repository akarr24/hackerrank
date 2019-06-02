#!/bin/python3

import sys

def solve(grades):
    output = []
    for grade in grades:
        if grade < 38:
            output.append(grade)
        else:
            new_grade = (int(grade / 5) + 1) * 5
            if new_grade - grade < 3:
                output.append(new_grade)
            else:
                output.append(grade)
    return output   

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))



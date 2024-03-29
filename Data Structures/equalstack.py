# -*- coding: utf-8 -*-
#!/bin/python3

import os
import sys

#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3, n1, n2, n3):
    #
    # Write your code here.
    #
    sum1 = sum2 = sum3 = 0
    for i in range(len(h1)):
        sum1 += h1[i]
    
    for i in range(len(h2)):
        sum2 += h2[i]
    
    for i in range(len(h3)):
        sum3 += h3[i]
    
    top1, top2, top3 = 0, 0, 0

    while (1): 
      # If any stack is empty 
        if (top1 == n1 or top2 == n2 or top3 == n3): 
            return 0
   
      # If sum of all three stack are equal. 
        if (sum1 == sum2 and sum2 == sum3): 
            return sum1 
       
      # Finding the stack with maximum sum and  
      # removing its top element. 
        if (sum1 >= sum2 and sum1 >= sum3): 
            sum1 -= h1[top1] 
            top1 += 1
        elif (sum2 >= sum3 and sum2 >= sum3): 
            sum2 -= h2[top2] 
            top2 += 1
        elif (sum3 >= sum2 and sum3 >= sum1): 
            sum3 -= h3[top3] 
            top3 += 1
    



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3, n1, n2, n3)

    fptr.write(str(result) + '\n')

    fptr.close()



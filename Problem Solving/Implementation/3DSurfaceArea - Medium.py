#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#

def surfaceArea(A):
    # Write your code here
    height = len(A)
    width = len(A[0])
    topBottom = height * width
    surfaceArea = topBottom * 2
    
    for i in range(height):
        for j in range(width):
            currentHeight = A[i][j]
            if i == 0:
                surfaceArea += currentHeight
            else:
                surfaceArea += max(currentHeight - A[i-1][j], 0)
            if i == height - 1:
                surfaceArea += currentHeight
            else:
                surfaceArea += max(currentHeight - A[i+1][j], 0)
            if j == 0:
                surfaceArea += currentHeight
            else:
                surfaceArea += max(currentHeight - A[i][j-1], 0)
            if j == width -1 :
                surfaceArea += currentHeight
            else:
                surfaceArea += max(currentHeight - A[i][j+1], 0)

    
    return surfaceArea            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'connectedCell' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def get_region_size(matrix, row, col, visited):
    # Check if the current cell is out of bounds or already visited or empty
    if (row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or
        visited[row][col] or matrix[row][col] == 0):
        return 0
    
    visited[row][col] = True
    
    size = 1
    for r in range(row-1, row +2):
        for c in range(col - 1, col + 2):
            if r != row or c != col:
                size += get_region_size(matrix, r, c, visited)

     
    return size
    

def connectedCell(matrix):
    largest_region_size = 0
    visited = [[False for col in range(len(matrix[0]))] for row in range(len(matrix))]
    
    
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1 and not visited [row][col]:
                region_size = get_region_size(matrix, row, col, visited)
                if region_size > largest_region_size:
                    largest_region_size = region_size
                    
    
    return largest_region_size
    
            
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    m = int(input().strip())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)

    fptr.write(str(result) + '\n')

    fptr.close()
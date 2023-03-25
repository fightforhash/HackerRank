#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        
    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i + 1


def quickSort(arr):
    n = len(arr)
    
    if n <= 1:
        return arr
    
    pivot_idx = n // 2
    pivot = arr[pivot_idx]
    
    left = [arr[i] for i in range(n) if arr[i] < pivot or (arr[i] == pivot and i < pivot_idx)]
    right = [arr[i] for i in range(n) if arr[i] > pivot or (arr[i] == pivot and i > pivot_idx)]
    
    left_sorted = quickSort(left)
    right_sorted = quickSort(right)
    
    return left_sorted + [pivot] + right_sorted
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
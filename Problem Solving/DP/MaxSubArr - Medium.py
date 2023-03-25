#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarray(arr):
    # Write your code here
    n = len(arr)
    best_sum = arr[0]
    curr_sum = arr[0]
    cont_sum = arr[0]
    for i in range(1, n):
        curr_sum = max(curr_sum + arr[i], arr[i])
        best_sum = max(best_sum, curr_sum)
        cont_sum = max(cont_sum, arr[i], cont_sum + arr[i])
    return [best_sum, cont_sum]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

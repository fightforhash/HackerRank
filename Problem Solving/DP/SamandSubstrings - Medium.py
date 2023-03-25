#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'substrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING n as parameter.
#

def substrings(n):
    # Write your code here
    ans = int(n[0])
    mod = 10 ** 9 + 7
    prevsum = int(n[0])
    prevdigit = int(n[0])
    
    for i in range(1, len(n)):
        digit = int(n[i])
        prevsum = (prevsum * 10 + (i+1) * digit) % mod
        ans = (ans + prevsum) % mod
            
            
    return ans 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = input()

    result = substrings(n)

    fptr.write(str(result) + '\n')

    fptr.close()

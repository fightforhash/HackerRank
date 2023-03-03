{\rtf1\ansi\ansicpg1252\cocoartf2638
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 HelveticaNeue;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw5760\paperh8640\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab560
\pard\pardeftab560\slleading20\partightenfactor0

\f0\fs26 \cf0 \
#!/bin/python3\
\
import math\
import os\
import random\
import re\
import sys\
\
#\
# Complete the 'quickSort' function below.\
#\
# The function is expected to return an INTEGER_ARRAY.\
# The function accepts INTEGER_ARRAY arr as parameter.\
#\
def partition(arr, low, high):\
    pivot = arr[high]\
    i = low - 1\
    \
    for j in range(low, high):\
        if arr[j] <= pivot:\
            i += 1\
            arr[i], arr[j] = arr[j], arr[i]\
        \
    arr[i+1], arr[high] = arr[high], arr[i+1]\
\
    return i + 1\
\
\
def quickSort(arr):\
    n = len(arr)\
    \
    if n <= 1:\
        return arr\
    \
    pivot_idx = n // 2\
    pivot = arr[pivot_idx]\
    \
    left = [arr[i] for i in range(n) if arr[i] < pivot or (arr[i] == pivot and i < pivot_idx)]\
    right = [arr[i] for i in range(n) if arr[i] > pivot or (arr[i] == pivot and i > pivot_idx)]\
    \
    left_sorted = quickSort(left)\
    right_sorted = quickSort(right)\
    \
    return left_sorted + [pivot] + right_sorted\
    \
    \
if __name__ == '__main__':\
    fptr = open(os.environ['OUTPUT_PATH'], 'w')\
\
    n = int(input().strip())\
\
    arr = list(map(int, input().rstrip().split()))\
\
    result = quickSort(arr)\
\
    fptr.write(' '.join(map(str, result)))\
    fptr.write('\\n')\
\
    fptr.close()\
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0
\cf0 \
}
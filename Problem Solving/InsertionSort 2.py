{\rtf1\ansi\ansicpg1252\cocoartf2638
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 HelveticaNeue;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw5760\paperh8640\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab560
\pard\pardeftab560\slleading20\partightenfactor0

\f0\fs26 \cf0 Insertion Sort 2 \
\
#!/bin/python3\
\
import math\
import os\
import random\
import re\
import sys\
\
#\
# Complete the 'insertionSort2' function below.\
#\
# The function accepts following parameters:\
#  1. INTEGER n\
#  2. INTEGER_ARRAY arr\
#\
\
def insertionSort2(n, arr):\
    # Write your code here\
    for i in range(1, len(arr)):\
        key = arr[i]\
        j = i-1\
        \
        while j >= 0 and key < arr[j]:\
            arr[j+1] = arr[j]\
            j-=1\
        arr[j+1] = key\
        print(" ".join(str(x) for x in arr))\
        \
    \
if __name__ == '__main__':\
    n = int(input().strip())\
\
    arr = list(map(int, input().rstrip().split()))\
\
    insertionSort2(n, arr)\
}
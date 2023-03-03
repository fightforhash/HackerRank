{\rtf1\ansi\ansicpg1252\cocoartf2638
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 HelveticaNeue;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw5760\paperh8640\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab560
\pard\pardeftab560\slleading20\partightenfactor0

\f0\fs26 \cf0 #!/bin/python3\
\
import math\
import os\
import random\
import re\
import sys\
\
#\
# Complete the 'formingMagicSquare' function below.\
#\
# The function is expected to return an INTEGER.\
# The function accepts 2D_INTEGER_ARRAY s as parameter.\
#\
def reflect(arr):\
    rft = []\
    for i in range(3):\
        lst = []\
        for j in range(2, -1, -1):\
            lst.append(arr[i][j])\
        rft.append(lst)\
    return rft\
\
def rotate(arr):\
    rot = []\
    for j in range(3):\
        lst = []\
        for i in range(2, -1, -1):\
            lst.append(arr[i][j])\
        rot.append(lst)\
    return rot\
\
def total(s, arr):\
    total = 0\
    for i in range(3):\
        for j in range(3):\
            total += abs(s[i][j] - arr[i][j])\
    return total\
\
def formingMagicSquare(s):\
    square = [[4,3,8], [9,5,1], [2,7,6]]\
    totals = []\
    for tot in range(4):\
        totals.append(total(s, square))\
        ref_ms = reflect(square)\
        totals.append(total(s, ref_ms))\
        square = rotate(square)\
    return min(totals)\
        \
if __name__ == '__main__':\
    fptr = open(os.environ['OUTPUT_PATH'], 'w')\
\
    s = []\
\
    for _ in range(3):\
        s.append(list(map(int, input().rstrip().split())))\
\
    result = formingMagicSquare(s)\
\
    fptr.write(str(result) + '\\n')\
\
    fptr.close()\
}
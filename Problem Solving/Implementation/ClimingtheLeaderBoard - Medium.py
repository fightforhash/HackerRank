#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    scores_set = list(set(ranked))
    scores_set.sort(reverse = True)
    
    result = []
    l = len(scores_set)
    
    for s in player:
        while (l > 0) and (s >= scores_set[l-1]):
            l -=1
        result.append(l+1)
    return result
    
    
    
    return result
        
    

    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

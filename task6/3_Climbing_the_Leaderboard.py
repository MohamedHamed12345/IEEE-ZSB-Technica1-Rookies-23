#!/bin/python3

import math
import os
import random
import re
import sys
def climbingLeaderboard(ranked, player):
    l=list(set(ranked))
    l.sort()
    l.reverse()
    lr=[]
    cur=len(l)-1
    for i in (player):
        b=True
        for j in range(cur,-1,-1):
            if i<l[j]:
                cur=j
                b=False
                break
        if b==True: 
            lr.append(1)    
        elif b==False:
           lr.append(j+2)
    return lr
if __name__ == '__main__':
    ranked_count = int(input().strip())
    ranked = list(map(int, input().rstrip().split()))
    player_count = int(input().strip())
    player = list(map(int, input().rstrip().split()))
    result = climbingLeaderboard(ranked, player)
    print('\n'.join(map(str, result)))


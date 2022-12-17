import collections
import heapq
import sys
import math
import itertools
#from bisect import bisect_left,bisect_right,insort
import os
# sys.setrecursionlimit(10000)
index=[(1,0),(0,1),(-1,0),(0,-1),(0,0)]
input = sys.stdin.readline
def solve():
    l=[]
    for i in range(3):l.append(list(map(int,input().strip().split())))
    dp=[[1]*3 for _ in range(3)]
    
    def get(u,v):
        for i,j  in index:
           
                if 0<=i+u<3 and 0<=j+v<3:dp[i+u][j+v]^=1
                    

    for i in range(3):
        for j in range(3):
            while l[i][j]:
                get(i,j); l[i][j]-=1
    for el in dp:print("".join([str(i) for i in el]))
        

if __name__ == '__main__':
#    for i in range(int(input())):
      solve()

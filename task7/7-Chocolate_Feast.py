import collections
import heapq
import sys
import math
import itertools
#from bisect import bisect_left,bisect_right,insort
import os
# sys.setrecursionlimit(10000)
input = sys.stdin.readline
def solve():
    n,c,m=list(map(int,input().strip().split()))
    tot=num=n//c
    while num>=m:
        tmp=num//m
        num-=m*tmp;tot+=1*tmp
        num+=tmp
    print(tot)
    

if __name__ == '__main__':
   for i in range(int(input())):
      solve()

import collections
import heapq
import sys
import math
import itertools
import bisect
import os
from io import BytesIO, IOBase
input = sys.stdin.readline
def solve():
    n,d=list(map(int, input().split()))
    arr=list(map(int, input().split()))
    tot=0
    
    mp=collections.defaultdict(lambda:[0,0])
    c=collections.Counter()
    for i,el in enumerate(arr) : 
        if el>=d:mp[i][0]+=c[el-d]
        c[el]+=1
    c.clear()
    for i in range(n-1,-1,-1) : 
        mp[i][1]+=c[arr[i]+d]
        c[arr[i]]+=1
    for i in mp:
         tot+=mp[i][0]*mp[i][1]
 
    print(tot)

    

if __name__ == '__main__':
#    for i in range(int(input())):
      solve()
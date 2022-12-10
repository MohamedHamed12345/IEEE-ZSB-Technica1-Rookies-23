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
    n,k=list(map(int, input().split()))
    l=collections.deque(map(int, input().split()))
    j=0
    while j<n and k:
       if j+1<len(l) and l[j+1]>l[j]:
          del l[j] ;k-=1
          if j!=0:j-=1
       else:
          j+=1
    print(*l)

    

if __name__ == '__main__':
   for i in range(int(input())):
      solve()
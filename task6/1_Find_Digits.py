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
    n = int(input())
    tot=0
    for i in str(n):
        if int(i)!=0:tot+=n%int(i)==0
    print(tot)
       

if __name__ == '__main__':
   for i in range(int(input())):
      solve()
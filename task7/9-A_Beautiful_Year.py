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
    n = int(input())+1
    while True :
        if len(set(str(n)))==len(str(n)):break
        else:n+=1
    print(n)

if __name__ == '__main__':
#    for i in range(int(input())):
      solve()

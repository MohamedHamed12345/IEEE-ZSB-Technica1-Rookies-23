import collections
import heapq
import sys
import math
import itertools
#from bisect import bisect_left,bisect_right,insort
import os
# sys.setrecursionlimit(10000)
input = sys.stdin.readline
def check(n):
    if n==1:return True
    s=str(n**2)
    rh=len(str(n))
    h=len(s)
    if 2*rh==h:
        return n==int(s[:rh])+int(s[rh:])
    elif h==2*rh-1:
        if int('0'+s[rh:]):
          return n==int(s[:rh])+int('0'+s[rh:]) or n==int(s[:rh-1])+int('0'+s[rh-1:])
    

def solve():
    a=int(input())
    b=int(input())
    l=[]
    for i in range(a,b+1):
        if check(i):l.append(i)
    if l:print(*l)
    else:print('INVALID RANGE')


if __name__ == '__main__':
#    for i in range(int(input())):
      solve()

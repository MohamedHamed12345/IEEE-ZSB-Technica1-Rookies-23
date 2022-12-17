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
    s=input().strip()
    tot=''
    while s:
       
        if len(s)>1 and s[0:2]=='--':tot+='2';s=s[2:]
        elif  len(s)>1 and s[0:2]=='-.':tot+='1';s=s[2:]
        elif s[0]=='.':tot+='0';s=s[1:]
    print(tot)
    

if __name__ == '__main__':
#    for i in range(int(input())):
      solve()

import collections
import heapq
import sys
import math
import itertools
import bisect
import os
import datetime
from io import BytesIO, IOBase
input = sys.stdin.readline


def solve():
    d1, m1, y1 = list(map(int, input().split()))
    d2, m2, y2 = list(map(int, input().split()))
    x=datetime.datetime(y1,m1,d1)-datetime.datetime(y2,m2,d2)
    if  x.days<0:return 0
    if y1 != y2:
        return 10000
    elif m1 != m2:
        return (abs(m1-m2))*500
    else:
        return abs(d1-d2) * 15


if __name__ == '__main__':
    print(solve())

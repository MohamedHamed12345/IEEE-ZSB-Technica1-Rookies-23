#!/bin/python3

import math
import os
import random
import re
import sys


def acmTeam(topic):
   d={}
   for i in range(0,len(topic)):
        for j in range(i+1,len(topic)):
           tem=0
           for h in range(len(topic[i])):
             if topic[i][h]=='1' or topic[j][h]=='1':
                tem+=1
           try:
                d[tem]+=1
           except:
                    d[tem]=1
   l=[]
   t=0
   for key in d.keys():
        t=max(t,key)
   l.append(t)
   l.append(d[t])
   return l

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    print('\n'.join(map(str, result)))


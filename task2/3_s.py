def solve():
        s='hello'
        t=input()
        si=0;ti=0
        while si<len(s) and ti<len(t):
            if  s[si] ==t[ti]:si+=1;ti+=1
            else:ti+=1
        if si==len(s) and (ti<len(t) or ti==len(t) and t[-1]==s[-1]):return 'yes'
        else:return 'no'


print(solve())
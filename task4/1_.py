import collections
n,k=list(map(int, input().split()))
l=collections.Counter(list(map(int, input().split())))
c=sorted(l.items(),key=lambda x:x[1],reverse=True)
print(*[i for i,j in c[:k]])
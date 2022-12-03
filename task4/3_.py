import collections
l=list(map(int, input().split()))
d=collections.defaultdict(lambda:[-1,len(l)+1])
for i,j in enumerate(l):
    if j in d: d[j][1]=i- d[j][0]
    d[j][0]=i
mx=min([d[i][1] for i in d])  
print(mx)

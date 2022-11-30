r=0;s=[]
for i in range(int(input())):
    a,b=list(map(int, input().split()))
    r+=a
    s.append(b)
s=sorted(s)
print(r<=s[-1]+s[-2])
    

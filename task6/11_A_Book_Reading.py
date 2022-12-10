n,t=list(map(int, input().split()))
l=list(map(int, input().split()))
num=0
for i in l:
    num+=1
    t-=86400-i
    if t<=0:break
print(num)
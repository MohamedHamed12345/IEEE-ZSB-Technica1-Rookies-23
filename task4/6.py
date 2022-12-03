def get(n,i):
    n=sorted(list(str(n)))
    if i:return int("".join(n))
    return int("".join(n[::-1]))

n=int(input())
num=0
while True:
    num+=1
    tmpn=abs(get(n,1)-get(n,0))
    if tmpn==n:break
    n=tmpn
    
print(num)
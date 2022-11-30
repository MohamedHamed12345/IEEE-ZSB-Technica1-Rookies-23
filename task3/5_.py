n,m=list(map(int, input().split()))
l=list(map(int, input().split()))
mx=max([l[i]-l[i-1] for i in range(1,m)])
print(max((mx+1)//2,l[0],n-1-l[-1]))

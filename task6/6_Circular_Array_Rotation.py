n,k,q=list(map(int, input().split()))
arr=list(map(int, input().split()))
idx=list(int(input()) for _ in range(q))
k=k%n
arr=arr[-k:]+arr[:-k]
for i in idx:print(arr[(i)])


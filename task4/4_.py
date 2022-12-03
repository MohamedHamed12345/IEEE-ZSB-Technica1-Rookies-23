n=int(input())
l=list(map(int, input().split()))
l=list(str(int("".join([str(i) for i in l]))+1))
print(*l)
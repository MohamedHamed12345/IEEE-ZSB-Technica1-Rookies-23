l=[list(map(int, input().split())) for i in range(int(input()))]
l=list(zip(*l[::-1]))
for i in l:print(*i)
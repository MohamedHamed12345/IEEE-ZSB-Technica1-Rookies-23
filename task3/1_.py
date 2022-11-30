n=int(input())
l=[list(map(int, input().split())) for i in range(n)]
print(abs(sum([l[i][i] for i in range(n)])-sum([l[n-i-1][i] for i in range(n)])))

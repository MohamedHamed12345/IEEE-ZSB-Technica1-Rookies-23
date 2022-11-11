a=int(input())
print(int(str(a)[::-1]))
print("YES" if str(a)==str(a)[::-1] else "NO")

l = []
for _ in range(0,int(input())):
    l.append([input(), float(input())])
m=set([marks for name, marks in l])
second_highest = sorted(list(m))[1]
print('\n'.join([a for a,b in sorted(l) if b == second_highest]))

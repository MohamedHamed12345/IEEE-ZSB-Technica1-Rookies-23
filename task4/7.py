import  collections

def get(ss): return "".join(sorted(list(str(ss))))

d=collections.defaultdict(list)  
for i in range(int(input())) :
    s=input()
    d[get(s)].append(s)
for i in d:print(*d[i])
    

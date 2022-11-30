l=[[input(),float(input())] for i in range(int(input()))]
g=sorted(set([j for i,j in l]))[1]
f=filter(lambda x: abs(x[1]-g)<.000001,l)
for i ,j in list(f):print(i)


   


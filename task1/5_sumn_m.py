from math import lcm

n=int(input())
n3=n//3 
n5=n//5
lc=lcm(3,5)
nlc=n//lc
tot=3*n3*(n3+1)//2  +5*n5*(n5+1)//2-lc*nlc*(nlc+1)//2
print(tot)
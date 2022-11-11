n=input()
l=list(map(int, input().split()))
# s1=sum(l)    #1
#--------------------------
s2=0
for ele in l:s2+=ele       #2
#--------------------------
# s3=0
# for i in range(len(l)):s3+=l[i]       #3
#--------------------------
j=0;s4=0
while j<len(l):
    s4+=l[j];j+=1            #4
#--------------------------
def rec(idx):
    if idx==len(l):return 0
    return l[idx]+rec(idx+1)
s5=rec(0)                          #5
#--------------------------
print(s2,s4,s5)
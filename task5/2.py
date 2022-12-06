s=input()
stack=[]
d={'(':')','{':'}','[':']'}
for i in s:
    if stack and stack[-1] in d  and i==d[stack[-1]]:
        stack.pop()
    else:stack.append(i)
print(not len(stack)>0)

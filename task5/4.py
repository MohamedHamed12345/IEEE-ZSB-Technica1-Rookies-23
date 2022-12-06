import math,collections
def primeFactors(n):
    l=collections.deque()
    while n % 2 == 0:  l.append (2) ;n //= 2
    for i in range(3, int(math.sqrt(n))+1, 2): 
        while n % i == 0: l.append (i) ; n //= i
    if n > 2: l.append(n)  
    return l
print(*primeFactors(int(input())))

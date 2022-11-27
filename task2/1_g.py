import random 
def get(real ,nonreal ):
    real = list(str(real))
    nonreal=list(str(nonreal))
    hit=0;miss=0
    for i,j in enumerate(nonreal):
        if j==real[i]:hit+=1
        elif j in nonreal :continue
        elif j in real: miss+=1
    return (hit,miss)
   

def solve():
    a=int(random.random()*1000)
    t=1
    while True:
        print('guess the number')
        g=input()
        h,m=get(a,g)
        print(f'{h} hit {m} misses')
        if h ==3:
            print(f'good you guess the number correct with {t} iteration')
            break
        t+=1
      

solve()
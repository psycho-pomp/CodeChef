import math
t=int(input())
for _ in range(t):
    n=int(input())
    c=0
    while n>0:
        #print(math.floor(math.sqrt(n))**2)
        n-=math.floor(math.sqrt(n))**2
        #print(n)
        c+=1
    print(c)

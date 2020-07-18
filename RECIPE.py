# cook your dish here
import math
t=int(input())
for _ in range(t):
    x=list(map(int,input().split()))
    n=x[0]
    l=x[1:]
    g=l[0]
    for i in range(1,n):
        g=math.gcd(g,l[i])
    for i in range(n):
        l[i]//=g
    
    print(*l)

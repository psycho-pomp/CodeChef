# cook your dish here
import math
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    mi=1e19
    for i in range(n):
        for j in range(i+1,n):
            g=(a[i]*a[j])//(math.gcd(a[i],a[j]))
            mi=min(g,mi)
    print(int(mi))
            

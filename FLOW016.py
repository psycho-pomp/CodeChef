# cook your dish here
import math
t=int(input())
for _ in range(t):
    
    a,b=(map(int,input().split()))
    x=math.gcd(a,b)
    print(x,end=" ")
    print((a*b)//x)

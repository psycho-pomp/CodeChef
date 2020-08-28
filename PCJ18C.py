# cook your dish here
from fractions import Fraction
t=int(input())
for _ in range(t):
    #n=int(input())
    n,a,k=map(float,input().split())
    s=(n-2)*180
    d=(2*(s-(a*n)))/(n*(n-1))
    res=a+(k-1)*d
    if res==int(res):
        
        print(int(res),1)
    else:
        b=str(Fraction(res).limit_denominator())
        b=b.split("/")
        print(int(b[0]),int(b[1]))
    

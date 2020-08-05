# cook your dish here
import math 
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    k=0
    for i in a:
        if i%m==0:
            k+=1
    print(int(math.pow(2,k)-1))

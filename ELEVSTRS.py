# cook your dish here
from math import sqrt
t=int(input())
for _ in range(t):
    n,v1,v2=map(int,input().split())
    t1=n/v1
    t2=(sqrt(2)*n)/v2
    if t2>=t1:
        print("Stairs")
    else:
        print("Elevator")

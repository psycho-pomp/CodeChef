# cook your dish here
import math
t=int(input())
for _ in range(t):
    c,r=map(int,input().split())
    if math.ceil((c/9))<math.ceil(r/9):
        print(0,math.ceil((c/9)))
    else:
        print(1,math.ceil((r/9)))
        

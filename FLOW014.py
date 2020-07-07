# cook your dish here
t=int(input())
for _ in range(t):
    h,c,t=map(float,input().split())
    if h>50:
        h=1
    else:
        h=0
    if c<0.7:
        c=1
    else:
        c=0
    if t>5600:
        t=1
    else:
        t=0
    if c & t & h:
        print(10)
    elif h & c:
        print(9)
    elif c & t:
        print(8)
    elif h & t:
        print(7)
    elif h or c or t:
        print(6)
    else:
        print(5)
        

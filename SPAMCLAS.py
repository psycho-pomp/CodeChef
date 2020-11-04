import math
t=int(input())
for _ in range(t):
    n,minx,miny=map(int,input().split())
    x=minx
    y=minx+1
    for i in range(n):
        w,b=map(int,input().split())
        x=(x*w+b)%2
        y=(y*w+b)%2
    #print(x,y)
    if x%2==0 and y%2==0:
        print(miny-minx+1,0)
    elif x%2!=0 and y%2!=0:
        print(0,miny-minx+1)
    elif x%2==0 and y%2!=0:
        print(math.ceil((miny-minx+1)/2),math.floor((miny-minx+1)/2))
    elif x%2!=0 and y%2==0:
        print(math.floor((miny-minx+1)/2),math.ceil((miny-minx+1)/2))

t=int(input())
for _ in range(t):
    n,b=map(int,input().split())
    ma=0
    for i in range(n):
        w,h,p=map(int,input().split())
        if p<=b:
            area=w*h
            ma=max(ma,area)
    if ma==0:
        print("no tablet")
    else:
        print(ma)
            

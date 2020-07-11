# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    p=n//4
    x=a[p]
    y=a[(2*p)]
    z=a[(3*p)]
    f=1
    if x==a[p-1] or y==a[((2*p)-1)] or z==a[((3*p)-1)]:
        f=0
    if f:
        print(x,y,z)
    else:
        print(-1)
    

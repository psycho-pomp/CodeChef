t=int(input())
for _ in range(t):
    n,b,m=map(int,input().split())
    t=0
    while n!=0:
        
        if n%2==0:
            t+=(n//2)*m
            n=n//2
        else:
            t+=((n+1)//2)*m
            n-=(n+1)//2
        t+=b
        m*=2
        
    print(t-b)

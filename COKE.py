# cook your dish here
t=int(input())
for _ in range(t):
    
    n,m,k,l,r=map(int,input().split())
    cheap=10000000
    for i in range(n):
        c,p=map(int,input().split())
        if c>k:
            c-=m
            if c<k:
                c=k
        elif c<k:
            c+=m
            if c>k:
                c=k
        if l<=c<=r:
            cheap=min(cheap,p)
    if cheap==10000000:
        print(-1)
    else:
        print(cheap)
        
    

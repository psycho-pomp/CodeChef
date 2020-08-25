# cook your dish here
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    
    f=list(map(int,input().split()))
    p=list(map(int,input().split()))
    d={}
    for i in range(n):
        if f[i] in d:
            d[f[i]]+=p[i]
        else:
            d[f[i]]=p[i]
    print(min(d.values()))

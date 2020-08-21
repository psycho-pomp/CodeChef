# cook your dish here
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    curr=0
    res=0
    for i in range(n):
        if a[i]-curr<=k:
            curr=a[i]
        else:
            if (a[i]-curr)%k==0:
                res+=((a[i]-curr)//k)-1
            else:
                res+=(a[i]-curr)//k
            curr=a[i]
    print(res)

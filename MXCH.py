t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    l=list(range(n-k,n+1))+list(range(1,n-k))
    print(*l)

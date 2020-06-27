t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    x=n*(m-1)+m*(n-1)
    print(x)

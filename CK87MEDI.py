t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort()
    idx=(n+k)//2
    print(l[idx])

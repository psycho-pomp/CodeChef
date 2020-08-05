# cook your dish here
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort()
    print(sum(l[k:n-k])/(n-2*k))

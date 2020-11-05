# cook your dish here
t=int(input())
for _ in range(t):
    n,q=map(int,input().split())
    d=list(map(int,input().split()))
    qi=list(map(int,input().split()))
    mul=1
    for i in range(n):
        mul*=d[i]
    for i in range(q):
        qi[i]//=mul
    print(*qi)

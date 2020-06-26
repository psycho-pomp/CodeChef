t=int(input())
for _ in range(t):
    n=int(input())
    l=[0]*9
    for i in range(n):
        p,s=map(int,input().split())
        if 1<=p<=8:
            l[p]=max(l[p],s)
    print(sum(l))

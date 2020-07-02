t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    m=l[0]
    for i in range(1,n):
        m%=l[i]
    print(m)

t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    i=l.index(max(l))
    j=l.index(min(l))
    if i<j:
        print(max(l),min(l))
    else:
        print(min(l),max(l))

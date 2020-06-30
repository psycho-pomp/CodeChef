t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=[]
    if len(a)==len(set(a)):
        b=list(range(n-1,-1,-1))
    else:
        for i in range(n):
            x=n-1-i-a[i+1:].count(a[i])
            b.append(x)
    print(*b)

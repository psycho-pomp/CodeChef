def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    g=a[0]
    for i in range(1,n):
        g=gcd(g,a[i])
    if g==1:
        print(0)
    else:
        print(-1)

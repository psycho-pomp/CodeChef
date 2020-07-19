# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    m=10000000
    for i in range(1,n):
        m=min(m,(a[i]-a[i-1]))
    print(m)

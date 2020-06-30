# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    m=0
    for i in range(n):
        x=a[i]*20-b[i]*10
        m=max(m,x)
    print(m)

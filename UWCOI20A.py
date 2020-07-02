t=int(input())
for _ in range(t):
    n=int(input())
    m=0
    for i in range(n):
        m=max(m,int(input()))
    print(m)

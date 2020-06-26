t=int(input())
for i in range(t):
    n=int(input())
    s=0
    for j in range(1,n+1,2):
        s+=(n-j+1)*(n-j+1)
    print(s)

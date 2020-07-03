t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    m=0
    for i in range(1,n):
        m+=abs(l[i]-l[i-1])-1
    print(m)

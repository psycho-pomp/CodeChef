# cook your dish here
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    m=-1
    for i in range(n-k+1):
        #print(sum(a[i:i+k]))
        m=max(m,sum(a[i:i+k]))
    print(m)

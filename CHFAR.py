# cook your dish here
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    x=a.count(1)
    if k>=n-x:
        print("YES")
    else:
        print("NO")

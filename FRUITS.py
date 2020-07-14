# cook your dish here
t=int(input())
for _ in range(t):
    n,m,k=map(int,input().split())
    if n>m:
        x=n-m
        if x>k:
            print(x-k)
        else:
            print(0)
    else:
        x=m-n
        if x>k:
            print(x-k)
        else:
            print(0)

# cook your dish here
t=int(input())
for _ in range(t):
    sd=0
    n,k=map(int,input().split())
    for i in range(n):
        t,d=map(int,input().split())
        if k>=t:
            k=k-t
        else:
            sd+=(t-k)*d
            k=0
    print(sd)

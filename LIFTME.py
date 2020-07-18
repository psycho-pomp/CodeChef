# cook your dish here
t=int(input())
for _ in range(t):
    n,q=map(int,input().split())
    s=0
    x=0
    for i in range(q):
        f,d=map(int,input().split())
        s+=abs(f-x)+abs(d-f)
        x=d
    print(s)

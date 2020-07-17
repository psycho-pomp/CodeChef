# cook your dish here
# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort()
    b.sort()
    s=0
    for i,j in zip(a,b):
        s+=min(i,j)
    print(s)

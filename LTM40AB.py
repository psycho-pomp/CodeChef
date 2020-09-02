# cook your dish here
t=int(input())
for _ in range(t):
    a,b,c,d=(map(int,input().split()))
    res=0
    for x in range(a,b+1):
        res+=max(d-(max(c,x+1))+1,0)
    print(res)

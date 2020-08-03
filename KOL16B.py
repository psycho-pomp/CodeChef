# cook your dish here
t=int(input())
for k in range(1,t+1):
    n=int(input())
    a=[]
    b=[]
    for i in range(n):
        x=int(input())
        b.append(x>>16)
        a.append(x-(b[i]<<16))
    print("Case %d:"%k)
    print(*a)
    print(*b)

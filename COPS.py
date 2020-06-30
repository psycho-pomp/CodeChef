# cook your dish here
t=int(input())
for _ in range(t):
    m,x,y=map(int,input().split())
    l=list(map(int,input().split()))
    p=x*y
    s=[]
    for i in range(m):
        lower=max(1,l[i]-p)
        upper=min(100,l[i]+p)
        s+=list(range(lower,upper+1))
    #print(set(s))
    print(100-len(set(s)))

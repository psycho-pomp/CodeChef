# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    d=list(map(int,input().split()))
    res=[]
    for i in range(n):
        if i==n-1:
            #print(d[i],a[i-1],a[0])
            if (d[i]>a[i-1]) and (d[i]>a[0]) and (d[i]>(a[i-1]+a[0])):
                res.append(d[i])
        else:
            #print(d[i],a[i-1],a[i+1])
            if (d[i]>a[i-1]) and (d[i]>a[i+1]) and (d[i]>(a[i-1]+a[i+1])):
                res.append(d[i])

    if len(res)!=0:
        print(max(res))
    else:
        print(-1)
            

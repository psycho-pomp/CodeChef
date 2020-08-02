# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    s=0
    res=0
    for i in range(n):
        s+=a[i]
        if s==i+1:
            res+=0
        else:
            if a[i]==1:
                res+=100
            else:
                res+=1100
    print(res)
            

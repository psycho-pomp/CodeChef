t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    p=0
    x=0
    for i in range(n):
        #print(p)
        if a[i]-p>=b[i]:
            x+=1
        p=a[i]
    print(x)
    

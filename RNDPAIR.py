# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    m=[]
    for i in range(n):
        for j in range(i+1,n):
            m.append(a[i]+a[j])
    y=m.count(max(m))
    x=(n-1)*(n)/2
    #print("{:.8f}".format(y/x))
    print ('%.8f'%(y/x))

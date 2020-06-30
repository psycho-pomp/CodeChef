t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    s=0
    p=k
    flag=1
    for i in range(n):
        s+=a[i]
        #print(s,p)
        if s<p:
            print("NO",end=' ')
            flag=0
            print(i+1)
            break
        p+=k
    if flag:
        print("YES")

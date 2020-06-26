t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    s=''
    for i in l:
        if i<=k:
            k-=i
            s+='1'
        else:
            s+='0'
        #print(k)
    print(s)

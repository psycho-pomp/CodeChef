# cook your dish here
t=int(input())
for _ in range(t):
    n,x,s=map(int,input().split())
    lis=[0]*n
    lis[x-1]=1
    for i in range(s):
        a,b=map(int,input().split())
        if lis[a-1]==0 and lis[b-1]==0:
            continue
        else:
            lis[a-1],lis[b-1]=lis[b-1],lis[a-1]
    print(lis.index(1)+1)

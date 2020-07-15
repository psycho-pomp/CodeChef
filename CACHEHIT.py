# cook your dish here
t=int(input())
for _ in range(t):
    n,b,m=map(int,input().split())
    x=list(map(int,input().split()))
    flag=None
    res=0
    for i in x:
        if i//b!=flag:
            
            res+=1
            flag=i//b
    print(res)
    

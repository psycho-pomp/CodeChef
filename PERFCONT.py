# cook your dish here
t=int(input())
for _ in range(t):
    n,p=map(int,input().split())
    a=list(map(int,input().split()))
    x=p//10
    y=p//2
    hard=0
    easy=0
    for i in a:
        if i>=y:
            easy+=1
        elif i<=x:
            hard+=1
    if hard==2 and easy==1:
        print("yes")
    else:
        print("no")
            

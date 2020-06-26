t=int(input())
for _ in range(t):
    n,m,k=map(int,input().split())
    ml=list(map(int,input().split()))
    kl=list(map(int,input().split()))
    x=0
    y=0
    for i in range(1, n+1):
        if i in ml and i in kl:
            x+=1
        elif i not in ml and i not in kl:
            y+=1
    print(x,y)

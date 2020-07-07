t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    g=list(map(int,input().split()))
    front=0
    back=0
    for i in range(n):
        if g[i]-l[i]>=0:
            front+=1
        if g[n-i-1]-l[i]>=0:
            back+=1
    if front==back==n:
        print("both")
    elif front==n:
        print("front")
    elif back==n:
        print("back")
    else:
        print("none")

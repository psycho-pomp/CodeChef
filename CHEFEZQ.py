t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    w=0
    d=0
    for i in a:
        w+=i
        w-=k
        d+=1
        if w<0:
            break
    else:
        d+=(w//k)+1
    print(d)

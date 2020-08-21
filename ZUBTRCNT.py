t=int(input())
for _ in range(1,t+1):
    l,k=map(int,input().split())
    # cook your dish here
    if k<=l:
        n=l-k+1
        res=(n*(n+1))//2
        print("Case "+str(_)+": "+str(res))
    else:
        print("Case "+str(_)+": "+str(0))

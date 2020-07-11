t=int(input())
for _ in range(t):
    n=int(input())
    profit=0
    for i in range(n):
        s,p,v=map(int,input().split())
        profit=max(profit,((p//(s+1))*v))
    print(profit)

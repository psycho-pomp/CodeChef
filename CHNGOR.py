# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    cost=a[0]
    for i in range(1,n):
        cost|=a[i]
    print(cost)

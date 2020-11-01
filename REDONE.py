m=1e9+7
l=list(range(0,1000001))
for i in range(2,1000001):
    l[i]=(l[i-1]+l[i]+l[i]*l[i-1])%m
t=int(input())
for _ in range(t):
    n=int(input())
    print(int(l[n]))

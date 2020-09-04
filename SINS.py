import math
t=int(input())
for _ in range(t):
    x,y=(map(int,input().split()))
    print(2*math.gcd(x,y))


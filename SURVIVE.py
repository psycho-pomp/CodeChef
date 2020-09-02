# cook your dish here
import math
t=int(input())
for _ in range(t):
    n, k, s = map(int, input().split())
    if n < k or s > 6 and n * 6 < k * 7:
        print(-1)
    else:
        print(math.ceil((k * s )/ n))

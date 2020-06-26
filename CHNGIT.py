from collections import Counter
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    c=Counter(l)
    print(n-c.most_common(1)[0][1])

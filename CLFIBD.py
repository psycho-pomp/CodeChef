# cook your dish here
from collections import Counter
t=int(input())
for _ in range(t):
    s=input()
    d=sorted(list(Counter(s).values()))
    res="Dynamic"
    if len(d)>=4 and d[3]!=d[2]+d[1]:
        d[1],d[0]=d[0],d[1]
    for i in range(2,len(d)):
        if d[i]!=d[i-1]+d[i-2]:
            res="Not"
            break
    print(res)

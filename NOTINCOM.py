# cook your dish here
from collections import Counter
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    la=list(map(int,input().split()))
    lb=list(map(int,input().split()))
    da=Counter(la)
    res=0
    for i in set(la).intersection(lb):
        res+=da[i]
    print(res)
        

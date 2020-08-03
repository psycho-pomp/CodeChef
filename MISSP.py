# cook your dish here
from collections import Counter
t=int(input())
for _ in range(t):
    n=int(input())
    a=[]
    for i in range(n):
        a.append(int(input()))
    d=Counter(a)
    #print(d)
    for i in d:
        if d[i]%2!=0:
            print(i)
            break

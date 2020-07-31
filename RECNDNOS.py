# cook your dish here
from collections import Counter
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    d=Counter(a)
    #print(d)
    i=0
    while i<n-1:
        if  a[i]==a[i+1]:
            d[a[i]]-=1
            i+=2
        else:
            i+=1
        
    x=d.most_common(1)[0][1]
    res=d.most_common(1)[0][0]
    for i in d:
        if d[i]==x and i<res:
            res=i
    print(res)co

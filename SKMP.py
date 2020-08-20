from collections import Counter
t=int(input())
for _ in range(t):
    s=input()
    p=input()
    cs=Counter(s)
    cp=Counter(p)
    diff=cs-cp
    #print(cs,cp,diff)
    before,before1='',''
    after,after1='',''
    x=p[0]
    for i in sorted(diff.keys()):
        temp=i*diff[i]
        if i<=x:
            before+=temp
        elif i>x:
            after+=temp
        #print(temp)
    for i in sorted(diff.keys()):
        temp=i*diff[i]
        if i<x:
            before1+=temp
        elif i>=x:
            after1+=temp
    if (before+p+after)<(before1+p+after1):
        print(before+p+after)
    else:
        print(before1+p+after1)
        

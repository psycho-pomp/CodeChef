from collections import Counter
t=int(input())
for _ in range(t):
    f=1
    n=int(input())
    li=list(map(int,input().split()))
    d=Counter(li)
    x=list(d.values())
    if len(x)!=len(set(x)):
        print("NO")
    else:
        for i in d:
            z=li.index(i)
            y=d[i]
            #print(li[z:z+y],[i]*y)
            if li[z:z+y]!=[i]*y:
                f=0
                print("NO")
                break
        if f:
            print("YES")

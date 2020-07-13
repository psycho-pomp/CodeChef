# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    x=0
    a=[0,0]
    for i in range(2,n):
        if x not in a[:i-1]:
            a.append(0)
        else:
            j=i-2
            temp=0
            for k in range(j,-1,-1):
                temp+=1
                if x==a[k]:
                    break
            a.append(temp)
        x=a[i]
    #print(a)
    print(a[:n].count(a[n-1]))

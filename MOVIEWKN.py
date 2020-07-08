# cook your dish here
# cook your code here
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    r=list(map(int,input().split()))
    m=0
    p=r[0]
    idx=0
    for i in range(n):
        if l[i]*r[i]>m:
            m=l[i]*r[i]
            p=r[i]
            idx=i+1
        if l[i]*r[i]==m and r[i]>p:
            p=r[i]
            m=l[i]*r[i]
            idx=i+1
    print(idx)

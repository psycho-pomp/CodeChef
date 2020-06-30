# cook your dish here
def sumofdigits(num):
    r=0
    for i in str(num):
        r+=int(i)
    #print(r)
    return r
        
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    ma=-1
    for i in range(n):
        x=l[:i]+l[i+1:]
        #print(x)
        for j in x:
            p=j*l[i]
            ma=max(ma,sumofdigits(p))
    print(ma)

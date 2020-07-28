# cook your dish here
t=int(input())
for _ in range(t):
    s,n=map(int,input().split())
    c=0
    if s%2!=0:
        s-=1
        c+=1
    if s!=0:
        c+=s//min(n,s)
        if s%min(n,s):
            c+=1
    print(c)

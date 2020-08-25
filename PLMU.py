# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    c0=l.count(0)
    c2=l.count(2)
    x=(c0*(c0-1))//2
    y=(c2*(c2-1))//2
    
    
    print(x+y)

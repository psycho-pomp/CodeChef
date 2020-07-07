# cook your dish here
t=int(input())
for _ in range(t):
    n,a,b=map(int,input().split())
    x=list(map(int,input().split()))
    pa=x.count(a)/n
    pb=x.count(b)/n
    print(pa*pb)

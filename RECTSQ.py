# copied someone elses code
# cook your dish here
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    for i in range(max(n,m),0,-1):
        
        if n%i==0 and m%i==0:
            print((n*m)//(i*i))
            break

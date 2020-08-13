# cook your dish here
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    
    m=-1
    for i in range(k,0,-1):
        m=max(m,n%i)
    print(m)

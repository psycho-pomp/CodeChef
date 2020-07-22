# cook your dish here
t=int(input())
for _ in range(t):
    n,s=map(int,input().split())
    p=list(map(int,input().split()))
    a=list(map(int,input().split()))
    forward=101
    defender=101
    for i in range(n):
        if a[i]==0:
            defender=min(defender,p[i])
        else:
            forward=min(forward,p[i])
    if s+defender+forward>100:
        print('no')
    else:
        print("yes")
        

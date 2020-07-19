# cook your dish here
t=int(input())
for _ in range(t):
    n,k,v=map(int,input().split())
    l=list(map(int,input().split()))
    deleted_sum=((n+k)*v)-sum(l)
    if deleted_sum%k==0 and deleted_sum>0:
        print(deleted_sum//k)
    else:
        print(-1)

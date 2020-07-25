# cook your dish here
t=int(input())
for _ in range(t):
    l,r,k=map(int,input().split())
    if l==r:
        k=1
    print(k)

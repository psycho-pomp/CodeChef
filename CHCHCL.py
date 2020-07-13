# cook your dish here
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    if n%2==0 or m%2==0:
        print("Yes")
    else:
        print("No")

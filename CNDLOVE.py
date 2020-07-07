# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    if sum(l)%2==1:
        print("YES")
    else:
        print("NO")

t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    if n==len(set(l)):
        print("No")
    else:
        print("Yes")

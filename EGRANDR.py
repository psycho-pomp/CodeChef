# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    if 2 not in l and 5 in l and sum(l)/n>=4.0:
        print("Yes")
    else:
        print("No")

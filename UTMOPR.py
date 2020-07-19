# cook your dish here
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    if k==1:
        if sum(l)%2==0:
            print("odd")
        else:
            print("even")
    else:
        print("even")

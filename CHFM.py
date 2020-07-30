# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    temp=sum(l)
    if temp%n==0:
        if temp//n in l:
            print(l.index(temp//n)+1)
        else:
            print("Impossible")
    else:
        print("Impossible")

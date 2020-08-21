# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    nodds=0
    for i in l:
        if i%2!=0:
            nodds+=1
    if nodds%2==0:
        print(1)
    elif nodds==1 and n==1:
        print(1)
    else:
        print(2)

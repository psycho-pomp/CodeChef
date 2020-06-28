t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    f=list(input().split())
    l=[]
    for i in range(k):
        l+=list(input().split())
    for i in f:
        if i in l:
            print("YES",end=' ')
        else:
            print("NO",end=' ')
    print()
        

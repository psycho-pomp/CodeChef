t=int(input())
for _ in range(t):
    n=int(input())
    xenny=list(map(int,input().split()))
    yana=list(map(int,input().split()))
    xenny_first=0
    yana_first=0
    for i in range(n):
        if i%2==0:
            xenny_first+=xenny[i]
            yana_first+=yana[i]
        else:
            xenny_first+=yana[i]
            yana_first+=xenny[i]
    print(min(xenny_first,yana_first))
        
        

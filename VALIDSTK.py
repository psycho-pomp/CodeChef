t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    result='Valid'
    s=0
    for i in l:
        if i==1:
            s+=1
        elif i==0:
            s-=1
        if s<0:
            result='Invalid'
            break
    print(result)
    

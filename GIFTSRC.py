t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    flag=[]
    x=0
    y=0
    for i in range(0,n):
        if s[i] not in flag:
            if s[i]=='L':
                flag=['L','R']
                x-=1
            elif s[i]=='R':
                flag=['L','R']
                x+=1
            elif s[i]=='U':
                flag=['U','D']
                y+=1
            elif s[i]=="D":
                flag=['U','D']
                y-=1
    print(x,y)
            

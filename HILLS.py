# cook your dish here
t=int(input())
for _ in range(t):
    n,u,d=map(int,input().split())
    l=list(map(int,input().split()))
    curr=l[0]
    pos=1
    flag=True
    for i in range(1,n):
        if l[i]>curr and l[i]-curr<=u:
            curr=l[i]
            pos+=1
        elif l[i]==curr:
            curr=l[i]
            pos+=1
        elif l[i]<curr:
            if curr-l[i]<=d:
                curr=l[i]
                pos+=1
            elif curr-l[i]>d :
                if flag==True:
                    curr=l[i]
                    flag=False
                    pos+=1
                else:
                    break
        else:
            break
            
    print(pos)    

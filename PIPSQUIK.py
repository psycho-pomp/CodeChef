# cook your dish here
t=int(input())
for _ in range(t):
    n,h,y1,y2,l=map(int,input().split())
    count=0
    flag=True
    for i in range(n):
        t,x=map(int,input().split())
        if flag:
            if t==1:
                if h-y1<=x:
                    count+=1
                else:
                    l-=1
                    if l==0:
                        flag=False
                    else:
                        count+=1
            elif t==2:
                if y2>=x:
                    count+=1
                else:
                    l-=1
                    if l==0:
                        flag=False
                    else:
                        count+=1
    print(count)
        


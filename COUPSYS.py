# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    max1,max2,max3=0,0,0
    city1,city2,city3=0,0,0
    for i in range(n):
        c,l,x=map(int,input().split())
        if l==1:
            if x>max1:
                max1=x
                city1=c
            elif x==max1:
                if c<city1:
                    city1=c
            
        elif l==2:
            if x>max2:
                max2=x
                city2=c
            elif x==max2:
                if c<city2:
                    city2=c
        elif l==3:
            if x>max3:
                max3=x
                city3=c
            elif x==max3:
                if c<city3:
                    city3=c
    print(max1,city1)
    print(max2,city2)
    print(max3,city3)

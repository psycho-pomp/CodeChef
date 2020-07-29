# cook your dish here
t=int(input())
for _ in range(t):
    a,b,c,x,y=map(int,input().split())
    if x+y==a+b+c:
        temp=max(x,y)
        if a+b>=temp or a+c>=temp or b+c>=temp:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")

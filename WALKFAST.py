# cook your dish here
t=int(input())
for _ in range(t):
    n,a,b,c,d,p,q,y=map(int,input().split())
    city=list(map(int,input().split()))
    time=0
    a-=1
    b-=1
    d-=1
    c-=1
    time=abs(city[b]-city[a])*p
    if abs(city[c]-city[a])*p<=y :
        t=y+(abs(city[d]-city[c]))*q+(abs(city[b]-city[d]))*p
        print(min(time,t))
    else:
        print(time)

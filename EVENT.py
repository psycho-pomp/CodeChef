# cook your dish here
d={"saturday":0, "sunday":1, "monday":2, "tuesday":3, "wednesday":4, "thursday":5 ,"friday":6}
t=int(input())
for _ in range(t):
    s,e,l,r=input().split()
    l=int(l)
    r=int(r)
    min_interval=(d[e]-d[s]+8)%7
    total=0
    for i in range(0,101,7):
        if l<=min_interval+i<=r:
            ans=min_interval+i
            total+=1
    if total==1:
        print(ans)
    elif total>1:
        print("many")
    else:
        print("impossible")

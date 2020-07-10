# cook your dish here
t=int(input())
for _ in range(t):
    l=list(map(int,input().split()))
    s=input()
    u=set('abcdefghijklmnopqrstuvwxyz')
    z=list(u-set(s))
    #print(l)
    cost=0
    for i in z:
        cost+=l[(ord(i)-97)]
    print(cost)

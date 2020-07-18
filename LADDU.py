# cook your dish here
t=int(input())
for _ in range(t):
    x=list(input().split())
    activities=int(x[0])
    origin=x[1]
    total=0
    for i in range(activities):
        l=list(input().split())
        if l[0]=='CONTEST_WON':
            if 1<=int(l[1])<=20:
                total+=300+20-int(l[1])
            else:
                total+=300
        elif l[0]=='TOP_CONTRIBUTOR':
            total+=300
        elif l[0]=='BUG_FOUND':
            total+=int(l[1])
        elif l[0]=='CONTEST_HOSTED':
            total+=50
    if origin=='INDIAN':
        print(total//200)
    elif origin=='NON_INDIAN':
        print(total//400)
                

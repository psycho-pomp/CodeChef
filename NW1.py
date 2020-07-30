# cook your dish here
t=int(input())
for _ in range(t):
    w,s=input().split()
    d={"mon":0, "tues":1, "wed":2, "thurs":3, "fri":4, "sat":5,"sun":6}
    l=[4]*7
    if w=='31':
        i=d[s]
        l[i%7]+=1
        l[(i+1)%7]+=1
        l[(i+2)%7]+=1
    elif w=='30':
        i=d[s]
        l[i%7]+=1
        l[(i+1)%7]+=1
    print(*l)

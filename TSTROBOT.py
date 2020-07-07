# cook your dish here
t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    s=input()
    l=[]
    l.append(x)
    for i in s:
        if i=='L':
            x-=1
        elif i=='R':
            x+=1
        if x not in l:
            l.append(x)
    print(len(l))

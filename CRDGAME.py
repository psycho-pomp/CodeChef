# cook your dish here
def digitSum(num):
    s=str(num)
    res=0
    for i in s:
        res+=int(i)
    return res
        
t=int(input())
for _ in range(t):
    n=int(input())
    sa=0
    sb=0
    for i in range(n):
        a,b=map(int,input().split())
        if digitSum(a)>digitSum(b):
            sa+=1
        elif digitSum(b)>digitSum(a):
            sb+=1
        else:
            sb+=1
            sa+=1
    if sa>sb:
        print(0,sa)
    elif sb>sa:
        print(1,sb)
    else:
        print(2,sa)

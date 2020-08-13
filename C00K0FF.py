# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    flag=[False]*5
    for i in range(n):
        s=input()
        if s=="cakewalk":
            flag[0]=True
        elif s=="simple":
            flag[1]=True
        elif s=='easy':
            flag[2]=True
        elif s=="easy-medium" or s=="medium" :
            flag[3]=True
        elif s=='medium-hard' or s=='hard' :
            flag[4]=True
    if False in flag:
        print("No")
    else:
        print("Yes")

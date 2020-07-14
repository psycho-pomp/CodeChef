# cook your dish here
t=int(input())
for _ in range(t):
    s=(input())
    cu=0
    cd=0
    flag=""
    for i in s:
        if i!=flag:
            if i=='U':
                cu+=1
            else:
                cd+=1
            flag=i
    print(min(cu,cd))

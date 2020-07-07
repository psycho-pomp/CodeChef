# cook your dish here
t=int(input())
for _ in range(t):
    balance=0
    max_balance=0
    a=input()
    res=''
    for i in a:
        if i=='(':
            balance+=1
        elif i==')':
            balance-=1
        max_balance=max(max_balance,balance)
    #print(max_balance)
    for i in range(max_balance):
        res+='('
    for i in range(max_balance):
        res+=')'
    print(res)
    

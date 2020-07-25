# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    if (n-1)%8==0:
        print(str(n+3)+'LB')
    elif (n-4)%8==0:
        print(str(n-3)+'LB')
    elif (n-2)%8==0:
        print(str(n+3)+'MB')
    elif (n-5)%8==0:
        print(str(n-3)+'MB')
    elif (n-3)%8==0:
        print(str(n+3)+'UB')
    elif (n-6)%8==0:
        print(str(n-3)+'UB')
    elif (n+1)%8==0:
        print(str(n+1)+'SU')
    elif (n-0)%8==0:
        print(str(n-1)+'SL')
    

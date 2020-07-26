# cook your dish here
t=int(input())
for _ in range(t):
    x=input()
    y=input()
    z=''
    for i in range(len(x)):
        if x[i]==y[i]:
            if x[i]=='B':
                z+='W'
            else:
                z+='B'
        else:
            z+='B'
    print(z)
    ACBALL.py

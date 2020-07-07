# cook your dish here
t=int(input())
for _ in range(t):
    c=0
    for i in range(10):
        for j in list(map(int,input().split())):
            if j<=30:
                c+=1
    if c<60:
        print("no")
    else:
        print("yes")
                

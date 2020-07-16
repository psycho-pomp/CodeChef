# cook your dish here
t=int(input())
for _ in range(t):
    n,k=(map(int,input().split()))
    s=input()
    u=0
    l=0
    for i in s:
        if i.isupper():
            u+=1
        elif i.islower():
            l+=1
    if u<=k and l<=k:
        print("both")
    elif l<=k and u>k:
        print("brother")
    elif u<=k and l>k:
        print("chef")
    else:
        print("none")
            
    

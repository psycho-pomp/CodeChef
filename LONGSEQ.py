# cook your dish here
t=int(input())
for _ in range(t):
    n=input()
    n1=n.count("1")
    n0=n.count("0")
    if n1==1 or n0==1:
        print("Yes")
    else:
        print("No")
    

# cook your dish here
t=int(input())
for _ in range(t):
    H,P=map(int,input().split())
    if P>H//2:
        print(1)
    else:
        print(0)
        

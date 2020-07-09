# cook your dish here
t=int(input())
for _ in range(t):
    x,y,k=map(int,input().split())
    turns=(x+y)//k
    if turns%2==0:
        print("Chef")
    else:
        print("Paja")

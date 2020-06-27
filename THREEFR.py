t=int(input())
for _ in range(t):
    x,y,z=map(int,input().split())
    if 2*max(x,y,z)-(x+y+z)==0:
        print("yes")
    else:
        print("no")

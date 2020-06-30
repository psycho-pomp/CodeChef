t=int(input())
for _ in range(t):
    p1,p2,k=map(int,input().split())
    x=(p1+p2)//k
    if x%2!=0:
        print("COOK")
    else:
        print("CHEF")

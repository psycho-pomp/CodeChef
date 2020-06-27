t=int(input())
for _ in range(t):
    n=int(input())
    f=1
    for i in range(n,0,-1):
        f*=i
    print(f)

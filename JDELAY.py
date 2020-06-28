t=int(input())
for _ in range(t):
    n=int(input())
    c=0
    for i in range(n):
        s,j=map(int,input().split())
        
        if j-s>5:
            c+=1
    print(c)

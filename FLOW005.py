t=int(input())
for _ in range(t):
    n=int(input())
    c=0
    for i in [100,50,10,5,2,1]:
        c+=n//i
        n%=i
    print(c)
        

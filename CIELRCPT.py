t=int(input())
for _ in range(t):
    n=int(input())
    c=0
    for i in [2048,1024,512,256,128,64,32,16,8,4,2,1]:
        c+=n//i
        n=n%i
    print(c)
        

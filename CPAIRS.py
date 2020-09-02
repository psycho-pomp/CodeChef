# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    
    odd=[0]*n
    count=0
    for i in range(n):
        if a[i]%2!=0:
            count+=1
        odd[i]=count
    res=0       
    for i in range(n):
        if a[i]%2==0:
            res+=odd[n-1]-odd[i]
            
        
    print(res)

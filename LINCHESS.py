# cook your dish here
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    max_steps=k+1
    result=-1
    for i in l:
        if i<k and k%i==0:
            if k//i<max_steps:
                max_steps=k//i
                result=i
                
    print(result)

# cook your dish here
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    #res='NO'
    c=0
    for i in l:
        if i%2==0:
            c+=1
    if k==0:
        if c==n:
            print("NO")
        else:
            print("YES")
    else:
        if c>=k:
            print("YES")
        else:
            print("NO")
        

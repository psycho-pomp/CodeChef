# cook your dish here
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    c=0
    
    l.sort(reverse=True)
    x=l[k-1]
    for i in l:
        if i>=x:
            c+=1
    print(c)

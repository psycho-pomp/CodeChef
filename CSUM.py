# cook your dish here
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    res="No"
    s=set()
    for i in range(n):
        if k-a[i] in s:
            res="Yes"
            break
        s.add(a[i])
            
        
    print(res)

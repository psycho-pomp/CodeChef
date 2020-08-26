# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort(reverse=True)
    result=0
    for i in range(n):
        if l[i]-i>0:
            result+=l[i]-i
    
    print(result%1000000007)
            

# cook your dish here
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(input().split())
    x=n-k
    while n!=x:
        n-=1
        if a[-1]=='H':
            del a[-1]
            for j in range(n):
                if a[j]=='H':
                    a[j]='T'
                else:
                    a[j]='H'
        else:
            del a[-1]
        #print(a)
    print(a.count("H"))
        

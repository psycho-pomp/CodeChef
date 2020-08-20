# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort(reverse=True)
    first=0
    second=0
    for i in range(n):
        if i==0:
            first+=l[i]
        elif i==1 or i==2:
            second+=l[i]
        else:
            if i%2==1:
                first+=l[i]
            else:
                second+=l[i]
    if first>second:
        print("first")
    elif second>first:
        print("second")
    else:
        print("draw")
    
    

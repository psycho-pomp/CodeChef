# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    m=int(input())
    b=list(map(int,input().split()))
    res="Yes"
    for i in b:
        if i in a:
            idx=a.index(i)
            a=a[idx+1:]
        else:
            res="No"
            break
    print(res)

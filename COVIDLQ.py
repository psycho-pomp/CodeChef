# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    prev=-6
    result="YES"
    for i in range(1,n+1):
        if l[i-1]==1 and i-prev>=6:
            prev=i
        elif l[i-1]==1 and i-prev<6:
            result='NO'
            break
    print(result)

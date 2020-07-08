# cook your dish here
t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    c=0
    result='NO'
    for i in range(n):
        if a[i]>=x:
            c+=1
        if c>=1:
            result="YES"
            break
    print(result)

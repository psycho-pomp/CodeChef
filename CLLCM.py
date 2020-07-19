# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    result='YES'
    for i in l:
        if i%2==0:
            result='NO'
            break
    print(result)
        

# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(input().split())
    result='YES'
    if l[n-1]=='cookie':
        result='NO'
    else:
        for i in range(n-1):
            if l[i]=='cookie' and l[i+1]!='milk':
                result='NO'
                break
    print(result)
    

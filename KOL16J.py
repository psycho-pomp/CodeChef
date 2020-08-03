# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    result="yes"
    flag=False
    if len(set(l))==n:
        for i in range(1,n+1):
            if i not in l:
                result="no"
                break
            else:
                if i!=l[i-1]:
                    flag=True
        if flag==False:
            result="no"
            
    else:
        result="no"
    print(result)

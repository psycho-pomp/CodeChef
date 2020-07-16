t=int(input())
for _ in range(t):
    l=list(map(int,input().split()))
    c=0
    result="#allcodersarefun"
    for i in l:
        if i==1:
            c+=1
        else:
            c=0
        if c>5:
            result="#coderlifematters"
            
    print(result)

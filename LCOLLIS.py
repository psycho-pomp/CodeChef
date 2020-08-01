def nCr(n,r):
    f = math.factorial
    return f(n) // (f(r) * f(n-r))
t=int(input())
for _ in range(t):
    r,c=map(int,input().split())
    matrix=[0]*c
    
    for i in range(r):
        k=0
        for j in input():
            if j=='1':
                matrix[k]+=1
            k+=1
    res=0
    for i in matrix:
        if i>=2:
            res+=nCr(i,2)
    print(res)

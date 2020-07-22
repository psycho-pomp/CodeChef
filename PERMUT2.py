# cook your dish here
n=int(input())
while n!=0:
    a=list(map(int,input().split()))
    result='ambiguous'
    for i in range(1,n+1):
        if i!=a[a[i-1]-1]:
            result='not ambiguous'
    n=int(input())
    print(result)
    

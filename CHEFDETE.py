n=int(input())
l=list(map(int,input().split()))
x=set(range(n+1))
x.difference_update(set(l))
print(*x)
        

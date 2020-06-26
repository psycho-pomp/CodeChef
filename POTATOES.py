def chk_prime(n):
    if n>1:
        for i in range(2, n//2+1):
            if n%i==0:
                return False
                break
        else:
            return True
    else:
        return False

t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    n=2147483647
    for i in range(x+y+1,n):
        if chk_prime(i):
            print(i-x-y)
            break

# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    i=5
    count=0
    while i<=n:
        count+=(n//i)
        i=i*5
    print(count)
        

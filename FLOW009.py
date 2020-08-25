# cook your dish here
t=int(input())
for _ in range(t):
    q,p=(map(int,input().split()))
    if q>1000:
        print(0.9*(q*p))
    else:
        print(q*p)

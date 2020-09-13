# cook your dish here
t=int(input())
for _ in range(t):
    g=int(input())
    for __ in range(g):
        i,n,q=(map(int,input().split()))
        even_flip=n//2
        odd_flip=n-n//2
        if i==q:
            print(even_flip)
        else:
            print(odd_flip)

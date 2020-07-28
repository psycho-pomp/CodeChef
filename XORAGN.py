# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    xor_a=l[0]
    for i in range(1,n):
        xor_a^=l[i]
    print(2*xor_a)

# cook your dish here
t=int(input())
for _ in range(t):
    n=input()
    c=int(n)
    for i in range(len(n)):
        c=min(c,int(n[:i]+n[i+1:]))
    print(c)

# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    s=str(n)
    if s==s[::-1]:
        print("wins")
    else:
        print("loses")

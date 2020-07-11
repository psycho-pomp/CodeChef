# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    print(n-max(s.count('R'),s.count("G"),s.count("B")))

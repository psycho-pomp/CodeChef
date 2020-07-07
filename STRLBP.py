# cook your dish here
t=int(input())
for _ in range(t):
    s=input()
    s=s+s[0]
    y=s.count("01")
    z=s.count("10")
    if y+z>2:
        print("non-uniform")
    else:
        print("uniform")

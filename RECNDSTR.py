# cook your dish here
t=int(input())
for _ in range(t):
    s=input()
    if (s[1:]+s[0:1])==(s[-1]+s[0:-1]) :
        print("YES")
    else:
        print("NO")

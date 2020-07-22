# cook your dish here
s=input()
x=set(s)
n=int(input())
for _ in range(n):
    w=input()
    if len(set(w).difference(x))==0:
        print("Yes")
    else:
        print("No")

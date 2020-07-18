# cook your dish here
t=int(input())
for _ in range(t):
    a=input()
    b=input()
    if len(set(a).intersection(set(b)))>0:
        print("Yes")
    else:
        print("No")

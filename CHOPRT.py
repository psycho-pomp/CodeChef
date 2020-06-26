t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    if n>m:
        print('>')
    elif n<m:
        print("<")
    else:
        print("=")

# cook your dish here
t=int(input())
for _ in range(t):
    n,start=input().split()
    a=list(map(int,input().split()))
    if int(n)==1 and a[0]%2==0 and start=='Dee':
        print("Dee")
    else:
        print("Dum")

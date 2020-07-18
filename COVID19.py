# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    smallest=n
    largest=0
    temp=1
    for i in range(1,n):
        if a[i]-a[i-1]<=2:
            temp+=1
        elif a[i]-a[i-1]>2:
            largest=max(largest,temp)
            smallest=min(smallest,temp)
            temp=1
    largest=max(largest,temp)
    smallest=min(smallest,temp)
    print(smallest,largest)

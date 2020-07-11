# cook your dish here
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    cost=0
    for i in l:
        if i>=k:
            ahead=((i//k)+1)*k-i
            back=i-((i//k)*k)
            if ahead<back:
                cost+=ahead
            elif back<ahead:
                cost+=back
            else:
                cost+=back
        else:
            cost+=((i//k)+1)*k-i
    print(cost)

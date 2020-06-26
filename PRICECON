t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    i_sum=0
    f_sum=0
    for x in range(n):
        i_sum+=l[x]
        if l[x]>k:
            f_sum+=k
        else:
            f_sum+=l[x]
    print(i_sum-f_sum)

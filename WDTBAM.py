# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    correct=input()
    chef=input()
    winning=list(map(int,input().split()))
    count=0
    for i in range(n):
        if chef[i]==correct[i]:
            count+=1
    if count==n:
        print(winning[n])
    else:
        print(max(winning[:(count+1)]))
        


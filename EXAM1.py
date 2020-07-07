# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    u=input()
    score=0
    i=0
    while i<n:
        if u[i]==s[i]:
            score+=1
            i+=1
        else:
            if u[i]=='N':
                i+=1
            else:
                i+=2
    print(score)

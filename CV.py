# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    c=0
    for i in range(0,n-1):
        if s[i] not in 'aeiou' and s[i+1] in 'aeiou':
            c+=1
    print(c)
            

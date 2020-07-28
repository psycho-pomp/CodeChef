# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    d={}
    for i in range(n):
        word,flag=input().split()
        if word not in d:
            d[word]=[flag]
        else:
            d[word].append(flag)
    c=0
    for i in d:
        c+=max(d[i].count('1'),d[i].count('0'))
    print(c)
        

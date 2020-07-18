# cook your dish here
r=int(input())
for _ in range(r):
    l=int(input())
    s=input()
    total=0
    result='Valid'
    for i in s:
        if i=='H':
            total+=1
        elif i=='T':
            total-=1
        if total<0 or total>1:
            result='Invalid'
            break
    if total!=0:
        result='Invalid'
    print(result)

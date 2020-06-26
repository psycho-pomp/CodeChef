t=int(input())
for _ in range(t):
    n=int(input())
    first_name=[]
    last_name=[]
    for i in range(n):
        first,last=input().split()
        first_name.append(first)
        last_name.append(last)
    for j in range(n):
        if first_name.count(first_name[j])>1:
            print(first_name[j]+" "+last_name[j])
        else:
            print(first_name[j])

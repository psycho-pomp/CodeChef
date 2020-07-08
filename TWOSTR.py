# cook your dish here
t=int(input())
for _ in range(t):
    x=input()
    y=input()
    result="Yes"
    for i in range(len(x)):
        if x[i]!='?' and y[i] !='?' and x[i]!=y[i]:
            result='No'
            break
    print(result)

# cook your dish here
t=int(input())
for _ in range(t):
    s=input()
    result='no'
    for i in s:
        if s.count(i)>1:
            result='yes'
            break
    print(result)

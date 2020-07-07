t=int(input())
for _ in range(t):
    s=input()
    l=len(s)
    result='NO'
    for i in s:
        if s.count(i)==l-s.count(i):
            result='YES'
            break
    print(result)

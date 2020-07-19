# cook your dish here
from collections import Counter
t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    d=Counter(s)
    result="YES"
    for i in d:
        if d[i]%2!=0:
            result='NO'
            break
    print(result)

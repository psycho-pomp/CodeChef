# cook your dish here
from collections import Counter
from sys import stdin,stdout
def get_ints():return map(int,stdin.readline().strip().split())
def get_array():return list(map(int,stdin.readline().strip().split()))
def get_string():return stdin.readline().strip()
def get_int():return int(stdin.readline().strip())
def op(c):return stdout.write(c)
t=get_int()
for _ in range(t):
    n=get_int()
    l=get_array()
    d=Counter(l)
    res=1
    c=0
    for i in sorted(d.keys(),reverse=True):
        if c>=2:
            break
        if d[i]==2 or d[i]==3:
            res*=i
            c+=1
        elif d[i]>=4:
            if c==0:
                res=i*i
                c+=2
            else:
                res*=i
                c+=1
    if c<2:
        op("-1\n")
    else:
        op(str(res)+"\n")

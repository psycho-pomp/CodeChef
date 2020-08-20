# cook your dish here
from sys import stdin,stdout
def get_ints():return map(int,stdin.readline().strip().split())
def get_array():return list(map(int,stdin.readline().strip().split()))
def get_string():return stdin.readline().strip()
def get_int():return int(stdin.readline().strip())
def op(c):return stdout.write(c)
taxes=[0,12500,25000,37500,50000,62500]
for _ in range(get_int()):
    n=get_int()
    tax=0
    if n<=250000:
        flag=0
        tax+=0
    elif 250000<n<500000:
        flag=1
        tax+=((n-250000)*0.05)
    elif 500000<n<=750000:
        flag=2
        tax+=((n-500000)*0.10)
    elif 750000<n<=1000000:
        flag=3
        tax+=((n-750000)*(0.15))
    elif 1000000<n<=1250000:
        flag=4
        tax+=((n-1000000)*0.2)
    elif 1250000<n<=1500000:
        flag=5
        tax+=((n-1250000)*0.25)
    elif n>1500000:
        flag=6
        tax+=((n-1500000)*0.3)
    tax+=sum(taxes[:flag])
    op(str(int(n-tax))+"\n")

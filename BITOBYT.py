# cook your dish here
from sys import stdin,stdout
def get_ints():return map(int,stdin.readline().strip().split())
def get_array():return list(map(int,stdin.readline().strip().split()))
def get_string():return stdin.readline().strip()
def get_int():return int(stdin.readline().strip())
def op(c):return stdout.write(c+"\n")
for _ in range(get_int()):
    n=get_int()
    if 1<=n%26<=2:
        print(2**(n//26),0,0)
    elif 3<=n%26<=10:
        print(0,2**(n//26),0)
    elif 11<=n%26:
        print(0,0,2**(n//26))
    elif n%26==0:
        print(0,0,2**((n//26)-1))

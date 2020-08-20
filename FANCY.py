# cook your dish here
from sys import stdin,stdout
def get_int():return int(stdin.readline().strip())
def get_array():return list(stdin.readline().strip().split())
def get_string():return stdin.readline().strip()
for _ in range(get_int()):
    s=get_array()
    if 'not' in s:
        print("Real Fancy")
    else:
        print("regularly fancy")

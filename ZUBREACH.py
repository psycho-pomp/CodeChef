# cook your dish here
from sys import stdin,stdout
def get_ints():return map(int,stdin.readline().strip().split())
def get_array():return list(map(int,stdin.readline().strip().split()))
def get_string():return stdin.readline().strip()
def get_int():return int(stdin.readline().strip()+"\n")
def op(c):return stdout.write(c)
for _ in range(1,get_int()+1):
    m,n=get_ints()
    rx,ry=get_ints()
    l=get_int()
    s=get_string()
    mov={'L':0,'R':0,'D':0,'U':0}
    for i in s:
        mov[i]+=1
    currx=mov['R']-mov['L']
    curry=mov['U']-mov['D']
    if currx<0 or curry<0 or currx>m or curry>n:
        print("Case "+str(_)+": "+"DANGER")
    elif currx==rx and curry==ry:
        print("Case "+str(_)+": "+"REACHED")
    else:
        print("Case "+str(_)+": "+"SOMEWHERE")
    

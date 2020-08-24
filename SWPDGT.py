# cook your dish here
from sys import stdin,stdout
def get_ints():return map(int,stdin.readline().strip().split())
def get_array():return list(map(int,stdin.readline().strip().split()))
def get_string():return stdin.readline().strip()
def get_int():return int(stdin.readline().strip())
def op(c):return stdout.write(c+"\n")
for _ in range(get_int()):
    s1,s2=stdin.readline().strip().split()
    l1=len(s1)
    l2=len(s2)
    if l1+l2==3:
        if l1==2:
            x=int(s1[0]+s2[0])+int(s1[1])
            y=int(s2[0]+s1[1])+int(s1[0])
            z=int(s1)+int(s2)
            print(max(x,y,z))
        elif l2==2:
            x=int(s2[0]+s1[0])+int(s2[1])
            y=int(s1[0]+s2[1])+int(s2[0])
            z=int(s1)+int(s2)
            print(max(x,y,z))
    elif l1+l2==4:
        w=int(s1)+int(s2)
        x=int(s2[0]+s1[1])+int(s1[0]+s2[1])
        y=int(s2[1]+s1[1])+int(s2[0]+s1[0])
        z=int(s1[0]+s2[0])+int(s1[1]+s2[1])
        print(max(x,y,z,w))
    else:
        print(int(s1)+int(s2))

from sys import stdin,stdout
def get_ints():return map(int,stdin.readline().strip().split())
def get_array():return list(map(int,stdin.readline().strip().split()))
def get_string():return stdin.readline().strip()
def get_int():return int(stdin.readline().strip())
def op(c):return stdout.write(c+"\n")
for _ in range(get_int()):
    n=get_int()
    a=get_array()
    count=1
    for i in range(1,n):
        if a[i]>a[i-1]:
            a[i]=a[i-1]
        else:
            count+=1
    op(str(count))
    

from sys import stdin,stdout
def get_ints():return map(int,stdin.readline().strip().split())
def get_array():return list(map(int,stdin.readline().strip().split()))
def get_string():return stdin.readline().strip()
def get_int():return int(stdin.readline().strip())
def op(c):return stdout.write(c+"\n")
for _ in range(get_int()):
    s1=get_string()
    s2=get_string()
    res='no'
    per=['bob','obb','bbo']
    if s1 in per:
        res='yes'
    elif s2 in per:
        res='yes'
    elif s1[0]+s2[1]+s2[2] in per:
        res='yes'
    elif s2[0]+s1[1]+s1[2] in per:
        res='yes'
    elif s2[0]+s1[1]+s2[2] in per:
        res='yes'
    elif s1[0]+s2[1]+s1[2] in per:
        res='yes'
    elif s2[0]+s2[1]+s1[2] in per:
        res='yes'
    elif s1[0]+s1[1]+s2[2] in per:
        res='yes'
    
    op(res)
    

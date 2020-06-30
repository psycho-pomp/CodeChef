t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    if 'Y' in s and 'I' not in s:
        print("NOT INDIAN")
    elif 'I' in s and 'Y' not in s:
        print("INDIAN")
    else:
        print("NOT SURE")

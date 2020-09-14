# cook your dish here
def sum_digits(n): return sum(map(int, str(n)))

def findRoundNumber(order):
    s = sum_digits(order) % 10
    return order * 10 + (0 if s == 0 else (10 - s))
t=int(input())
for _ in range(t):
    n=int(input())
    print(findRoundNumber(n))
    

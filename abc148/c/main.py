from math import gcd
def lcm(a, b):
    return int(a * b / gcd(a, b))
a, b = map(int, input().split())
print(lcm(a, b))
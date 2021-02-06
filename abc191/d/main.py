import math

x, y, r = map(float, input().split())

def cf(a, r):
    return math.ceil(a - r), math.floor(a + r)

cnt = 0

start, end = cf(x, r)

for i in range(start, end + 1):
    p = math.sqrt((r ** 2) - ((x - i) ** 2))
    bottom, top = cf(y, p)
    cnt += top + 1 - bottom

print(cnt)
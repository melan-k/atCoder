from math import floor
a, b = map(int, input().split())
# x * 0.08 = a
# y * 0.1 = b
# 100x * 8 = 100a
# 100x * 10 = 100b
print(floor(a / 0.08))
print(floor(a / 0.1))
if floor(a / 0.08) == floor(b / 0.01):
    print(floor(100 * a / 8))
else:
    print(-1)
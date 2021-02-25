n = int(input())
t, a = map(int, input().split())
heights = list(map(int, input().split()))

best = 100000
index = 0
for i, h in enumerate(heights):
    averate = (t - h * 0.006))
    if abs(a - average) < best:
        best = abs(a - average)
        index = i + 1
print(i)
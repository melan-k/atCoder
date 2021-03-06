n = int(input())
values = list(map(int, input().split()))
result = 0
for i in range(1, n):
    for j in range(i):
        result += (values[i] - values[j]) ** 2
print(result)
n, m = map(int, input().split())
available = set()
for i in range(m):
    start, end = map(int, input().split())
    if i == 0:
        available = set(range(start, end + 1))
    else:
        available &= set(range(start, end + 1))
print(len(available))
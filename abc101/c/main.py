n, k = map(int, input().split())
p = list(map(int, input().split()))
if n == k :
    print(1)
else:
    print(n // k + 1)
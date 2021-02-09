n, k = map(int, input().split())

if n % k == 0:
    print(0)
    exit()

if n <= abs(n - k):
    print(n)
    exit()


diff = abs(n - k)
if n % k >= diff:
    print(n % diff)
else:
    print(n % k)

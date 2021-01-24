n = int(input())
answer = ()
for i in range(1, n):
    if i ** 2 > n:
        break
    if n % i == 0:
        answer += tuple([i, n / i])

for a in sorted(answer):
    print(int(a))
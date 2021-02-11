n, k = map(int, input().split())
dices = list(map(int, input().split()))
e = 0
diffs = []
for i in range(n - k - 1):
    diffs.append(dices@)
for d in dices:
    print("{}'s ex : {}".format(d, sum(list(range(1, d+1))) / d))
    e += sum(list(range(1, d+1))) * 2 / d
print(e)

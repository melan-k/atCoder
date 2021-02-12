n, m = map(int, input().split())
submissions = {}
passed = []

if m == 0:
    print(0, 0)
    exit()

cnt = 0
for i in range(m):
    if n == len(passed):
        break

    p, s = input().split()
    p = int(p)

    if not p in submissions:
        submissions[p] = 0

    if s == 'AC':
        if not p in passed:
            passed.append(p)
            cnt += 1
    else:
        # WAが出た時
        if p in passed:
            continue

        if p in submissions:
            submissions[p] += 1

penalty = 0
for p in passed:
    penalty += submissions[p]
print(len(passed), penalty)
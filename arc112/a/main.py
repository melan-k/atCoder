import itertools

t = int(input())
for i in range(t):
    l, r = map(int, input().split())
    cnt = 0
    for comb in itertools.product(set(range(l, r + 1)), repeat=3):
    #     print(comb)
        if comb[2] == comb[0] + comb[1]:
            # print("{} - {} = {}".format(comb[2], comb[1], comb[0]))
            cnt += 1
    print(cnt)

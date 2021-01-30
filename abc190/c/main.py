n, m = map(int, input().split())
dishes = []
for i in range(m):
    dishes.append(list(map(int, input().split())))

k = int(input())
maps = {}
comb = []
for i in range(k):
    comb.append(list(map(int, input().split())))
    c, d = comb[i][0], comb[i][1]
    if c not in maps:
        maps[c] = 1
    else:
        maps[c] += 1
    if d not in maps:
        maps[d] = 1
    else:
        maps[d] += 1

print(maps)
# print(comb)

# 1種類ずつしかなく、その1種類の両方の皿で構成されている場合は除く
cnt = 0
for d in dishes:
    # print(d)
    if (d[0] in maps and d[1] in maps):
        if maps[d[0]] == 1:
            for c in comb:
                if c[0] == d[0]:
                    maps[c[1]] -= 1
        if maps[d[1]] == 1:
            for c in comb:
                if c[1] == d[1]:
                    maps[c[0]] -= 1
        # print('マップにある')
        if (maps[d[0]] == 1 and maps[d[1]] == 1) and d in comb:
            continue
        # print('数に余裕ある')
        cnt += 1

print(cnt)
x, k, d = map(int, input().split())

cnt = k
for i in range(k):
    cnt -= 1
    if x - d < 0:
        break
    if x != 0:
        x -= d

    if x == 0:
        if cnt %2 != 0:
            print(d)
        else:
            print(x)
        exit()
    # print(x, cnt)
    if cnt == 0:
        print(x)
        exit()

print(cnt)
if cnt %2 != 0:
    print(x)
else:
    print(d)
exit()
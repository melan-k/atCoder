from math import log10

def calc_digit(num):
    assert(num > 0)
    return int(log10(abs(num)) + 1)

n = int(input())
values = list(map(float, input().split()))

if 0 in values:
    print(0)
    exit()

result = 1.0
cnt = 0
for v in values:
    # 10の累乗をカウントする
    digit = calc_digit(v) - 1
    v /= 10.0 ** digit
    result *= v

    if result >= 10:
        result /= 10.0
        cnt += digit + 1
    else:
        cnt += digit

    print(v, digit)

print(int(result * (10 ** cnt)))
n = int(input())
values = list(map(int, input().split()))
mod_ = 1000000007
sum_ = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        # print(values[i], values[j])
        if sum_ < mod_:
            sum_ = mod_ - sum_
        sum_ += (values[i] * values[j]) % mod_
print(sum_)
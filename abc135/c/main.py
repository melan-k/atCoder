n = int(input())
enemies = list(map(int, input().split()))
power = list(map(int, input().split()))

total = 0
for i in range(n):
    total += min(power[i], enemies[i] + enemies[i + 1])
    enemies[i + 1] -= min(enemies[i] - power[i], 0)
print(total)
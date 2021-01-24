import math

n, k = map(int, input().split())

routes = math.factorial(n)
# １→各ルートへはそれぞれn-2通り行き方がある
# 各ルート→1へ戻るにはそれぞれn-2通り行き方がある

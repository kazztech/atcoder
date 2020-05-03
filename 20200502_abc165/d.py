import math

a, b, n = map(int, input().split(" "))

dp = [-1 for _ in range(b + 1)]

_max = 0
for i in range(n + 1):
    val = math.floor((a * i) / b) - (a * math.floor(i / b))
    print(val)
    if _max > 0 and val == 0: break
    _max = max(_max, val)

print(_max)
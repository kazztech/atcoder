import math

a, b, c, k = map(int, input().split(" "))

_sum = 0
if a >= k:
    print(k)
    exit()
else:
    _sum += a
    k -= a

if b >= k:
    print(_sum)
    exit()
else:
    k -= b

print(_sum - k)
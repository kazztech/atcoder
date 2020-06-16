import math

n, m = map(int, input().split(" "))
lrL = [list(map(int, input().split(" "))) for _ in range(m)]

_left, _right = 1, n

for l, r in lrL:
    _left = max(_left, l)
    _right = min(_right, r)

print(max(0, _right - _left + 1))

import math
from queue import Queue

n, m, k = map(int, input().split(" "))
aLi = list(map(int, input().split(" ")))
bLi = list(map(int, input().split(" ")))

a = [0 for _ in range(n + 1)]
b = [0 for _ in range(m + 1)]

aMax = k
bMax = k
for i in range(n):
    a[i + 1] = a[i] + aLi[i]
    if (a[i + 1] >= k):
        aMax = i + 1
        break
for i in range(m):
    b[i + 1] = b[i] + bLi[i]
    if (b[i + 1] >= k):
        bMax = i + 1
        break

_max = 0
for i, ai in enumerate((a[:aMax])):
    for j, bi in enumerate((b[:bMax])):
        if ai + bi <= k:
            _max = max(_max, i + j)

print(_max)
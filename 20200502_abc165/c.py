import math
import itertools

n, m, q = map(int, input().split(" "))
aL = []
_max = 0

for i in range(q):
    aL.append(list(map(int, input().split(" "))))

li = []


def dfs(i, _n, p):
    if i == n:
        li.append(list(map(int, list(str(_n)))))
        return
    for j in range(p, m + 1):
        dfs(i + 1, _n * 10 + j, j)


if m != 1:
    for i in range(1, m + 1):
        dfs(1, i, i)
else:
    li = [[i] for i in range(1, n + 1)]

for t in li:
    if t[0] == 0:
        continue
    _sum = 0
    for a in aL:
        if t[a[1] - 1] - t[a[0] - 1] == a[2]:
            _sum += a[3]
    _max = max(_max, _sum)

print(_max)
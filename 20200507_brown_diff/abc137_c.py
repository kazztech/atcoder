import math

n = int(input())


def cho(i):
    return (i * (i - 1)) // 2


d = {}
for i in range(n):
    s = "".join(sorted(input()))
    if s in d:
        d[s] += 1
    else:
        d[s] = 0

_ans = 0
for k, v in d.items():
    if v == 0: continue
    _ans += cho(v + 1)

print(_ans)

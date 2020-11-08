import math
import itertools

n = int(input())
ns = list(str(n))

ans = 10000000000
for c in itertools.product([0, 1], repeat=len(str(n))):
    ps = 0
    for index, i in enumerate(c):
        if i:
            ps += int(ns[index])
    if ps % 3 == 0 and ps != 0:
        ans = min(ans, c.count(0))

if ans == 10000000000:
    print(-1)
else:
    print(ans)
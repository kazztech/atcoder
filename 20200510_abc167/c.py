import math
import itertools

n, m, x = map(int, input().split(" "))
li = [list(map(int, input().split(" "))) for _ in range(n)]

_min = float("inf")

for i in range(n):
    for j in list(itertools.combinations(range(n), i + 1)):
        _sum = [0 for _ in range(m)]
        cost = 0
        for jj in j:
            cost += li[jj][0]
        for l in range(1, m + 1):
            for k in j:
                _sum[l - 1] += li[k][l]
        flg = True
        #print(_sum)
        for w in _sum:
            if x > w:
                flg = False
                break
        if flg:
            _min = min(_min, cost)
        # for k in range(j):
        #     print(li[])
        #     _sum += 1

if math.isinf(_min):
    print(-1)
else:
    print(_min)
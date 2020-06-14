import math
import itertools

n = int(input())
xys = [list(map(int, input().split(" "))) for _ in range(n)]

sums = []
for li in list(itertools.permutations(range(n))):
    _sum = 0
    for i in range(n):
        if i == n - 1: continue
        dx = abs(xys[li[i]][0] - xys[li[i + 1]][0])
        dy = abs(xys[li[i]][1] - xys[li[i + 1]][1])
        _sum += math.sqrt(dx**2 + dy**2)
    sums.append(_sum)

print(sum(sums) / len(sums))

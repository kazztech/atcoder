import math

n = int(input())
aL = list(map(int, input().split(" ")))
q = int(input())
bcL = [list(map(int, input().split(" "))) for _ in range(q)]

sums = [0 for i in range(10**5 + 1)]

for a in aL:
    sums[a] += 1

_sum = 0
for i, a in enumerate(sums):
    _sum += i * a

for b, c in bcL:
    _sum += (c - b) * sums[b]

    sums[c] += sums[b]
    sums[b] = 0
    print(_sum)
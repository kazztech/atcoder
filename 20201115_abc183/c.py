import math
import itertools

n, k = map(int, input().split(" "))
li = [list(map(int, input().split(" "))) for _ in range(n)]

cnt = 0
for pt in list(itertools.permutations(range(1, n))):
    cost = 0
    prev = 0
    for p in pt:
        cost += li[prev][p]
        prev = p
    cost += li[prev][0]
    if cost == k:
        cnt += 1

print(cnt)
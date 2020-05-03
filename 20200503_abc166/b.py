import math

n, k = map(int, input().split(" "))
pL = [0 for _ in range(n)]

for i in range(k):
    d = int(input())
    aL = list(map(int, input().split(" ")))
    for a in aL:
        pL[a - 1] += 1

ans = 0

for p in pL:
    if p == 0:
        ans += 1

print(ans)
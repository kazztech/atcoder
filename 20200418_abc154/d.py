import math

n, k = map(int, input().split(" "))
pL = list(map(int, input().split(" ")))

mx = 0
cs = 0
for i in range(k):
    cs += pL[i]
    mx = cs
for i in range(1, len(pL) - k + 1):
    cs = cs - pL[i - 1] + pL[i + k - 1]
    mx = max(mx, cs)
print((mx + k) / 2)
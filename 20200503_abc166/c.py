import math

n, m = map(int, input().split(" "))
hL = list(map(int, input().split(" ")))
hML = [True for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split(" "))
    if hL[a - 1] <= hL[b - 1]:
        hML[a - 1] = False
    if hL[b - 1] <= hL[a - 1]:
        hML[b - 1] = False

ans = 0
for b in hML:
    if b: ans += 1

print(ans)
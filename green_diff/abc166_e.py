import math

n = int(input())
aL = list(map(int, input().split(" ")))

d1 = {}
d2 = {}
for i in range(n):
    d1i = i - aL[i]
    d2i = i + aL[i]

    if d1i in d1:
        d1[d1i] += 1
    else:
        d1[d1i] = 1

    if d2i in d2:
        d2[d2i] += 1
    else:
        d2[d2i] = 1

ans = 0
for k, v in d2.items():
    if k in d1:
        ans += v * d1[k]

print(ans)
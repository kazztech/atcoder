import math

n, c = map(int, input().split(" "))
abcL = [list(map(int, input().split(" "))) for _ in range(n)]

sd = {}
for a, b, c2 in abcL:
    if a in sd:
        sd[a] += c2
    else:
        sd[a] = c2

    if b + 1 in sd:
        sd[b + 1] -= c2
    else:
        sd[b + 1] = -c2

sd = sorted(sd.items(), key=lambda x: x[0])
ans = 0
sm = 0
prev = 0
print(sd[:-1])
for pos, price in sd:
    sm += price
    if prev == 0 and sd[0][0] != 1:
        prev = pos
        continue
    if sm >= c:
        ans += (pos - prev) * c
    else:
        ans += sm * (pos - prev)
    prev = pos
print(ans)

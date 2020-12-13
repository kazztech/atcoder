import math

n, q = map(int, input().split(" "))
aL = list(map(int, input().split(" ")))
txyL = [list(map(int, input().split(" "))) for _ in range(q)]

cnt = 0
for t, x, y in txyL:
    if t == 2:
        s = aL[x - 1]
        for i in range(y - x):
            s ^= aL[x + i]
            cnt += 1
        print(s)
        continue
    if t == 1:
        aL[x - 1] = aL[x - 1] ^ y
        continue

print(cnt)
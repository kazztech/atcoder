import math
import itertools

n, m = map(int, input().split(" "))
sL = []
for i in range(m):
    _, *s = map(int, input().split(" "))
    sL.append(s)
pL = list(map(int, input().split(" ")))

bz = list(itertools.product([0, 1], repeat=n))
ans = 0
for b1 in bz:
    for i in range(m):
        s = sL[i]
        p = pL[i]
        cnt = 0
        for si in s:
            if b1[si - 1] == 1:
                cnt += 1
        if cnt % 2 != p:
            break
    else:
        ans += 1

print(ans)

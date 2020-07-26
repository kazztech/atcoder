import math

n = int(input())
aL = list(map(int, input().split(" "))) + [0]
bL = ["NO" for _ in range(n)]

mk = 0
mm = 1000

up = False
for i in range(n):
    cr = aL[i]
    nx = aL[i + 1]

    if up:
        if cr > nx:
            up = False
            mm += mk * cr
            mk = 0
    else:
        if cr < nx:
            up = True
            mk = mm // cr
            mm = mm % cr

print(mm)
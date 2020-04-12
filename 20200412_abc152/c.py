import math

n = int(input())
pL = list(map(int, input().split(" ")))

mi = pL[0]
cnt = 1

for i in range(1, len(pL)):
    if pL[i] < mi:
        cnt += 1
        mi = pL[i]

print(cnt)
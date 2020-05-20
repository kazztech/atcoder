import math

n = int(input())
hL = list(map(int, input().split(" ")))

cnt = 0
_max = 0
for i in range(len(hL) - 1):
    if hL[i] >= hL[i + 1]:
        cnt += 1
    else:
        _max = max(cnt, _max)
        cnt = 0

print(max(cnt, _max))
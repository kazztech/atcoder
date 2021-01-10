import math
import copy

n = int(input())
aL = list(map(int, input().split(" ")))
ansAL = copy.copy(aL)

cnt = len(aL)
offset = 0
while True:
    if cnt == 2:
        print(ansAL.index(min(aL[-1], aL[-2])) + 1)
        exit()
    for i in range(cnt // 2):
        i1 = i * 2
        i2 = i * 2 + 1
        aL.append(max(aL[offset + i1], aL[offset + i2]))
    offset += cnt
    cnt //= 2
import math

s = input()
li = [0 for _ in range(len(s))]

rCnt = 0
for i in range(len(s)):
    if s[i] == "R":
        rCnt += 1
    else:
        li[i] += rCnt // 2
        li[i - 1] += math.ceil(rCnt / 2)
        rCnt = 0
lCnt = 0
for i in reversed(range(len(s))):
    if s[i] == "L":
        lCnt += 1
    else:
        li[i] += lCnt // 2
        li[i + 1] += math.ceil(lCnt / 2)
        lCnt = 0

print(*li)
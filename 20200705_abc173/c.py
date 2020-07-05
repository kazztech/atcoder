import math
import itertools

h, w, k = map(int, input().split(" "))
cL = [input() for _ in range(h)]

blackCount = 0
for c in cL:
    for item in c:
        if item == "#":
            blackCount += 1

ans = 0
for x in range(w + 1):
    for y in range(h + 1):
        for x2 in itertools.combinations(range(w), x):
            for y2 in itertools.combinations(range(h), y):
                yCnt = 0
                xCnt = 0
                for y4 in y2:
                    # 該当のそれぞれのコマ数
                    xCnt += cL[y4].count("#")
                for x4 in x2:
                    for y3 in range(h):
                        if cL[y3][x4] == "#":
                            yCnt += 1
                th = 0
                for xa in x2:
                    for ya in y2:
                        if cL[ya][xa] == "#":
                            th += 1
                _sum = blackCount - yCnt - xCnt + th
                if k == _sum:
                    ans += 1

print(ans)
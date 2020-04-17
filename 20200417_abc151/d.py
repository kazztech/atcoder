import math
from queue import Queue
import copy

h, w = map(int, input().split(" "))
ili = [list(input()) for _ in range(h)]

q = Queue()
ans = 0

for y in range(h):
    for x in range(w):
        li = copy.deepcopy(ili)
        if li[y][x] == "#": continue
        q.put([x, y])
        li[y][x] = 0
        while not q.empty():
            c = q.get()
            # 上(0, -1) 右(1, 0) 下(0, 1) 左(-1, 0)
            for dr in [[0, -1], [1, 0], [0, 1], [-1, 0]]:
                nX = c[0] + dr[0]
                nY = c[1] + dr[1]

                if not (0 <= nX <= w - 1): continue
                if not (0 <= nY <= h - 1): continue

                if li[nY][nX] == ".":
                    li[nY][nX] = li[c[1]][c[0]] + 1
                    q.put([nX, nY])

        li = list(
            map(lambda item: 0 if item == "#" or item == "." else item,
                sum(li, [])))
        ans = max(li + [ans])

print(ans)
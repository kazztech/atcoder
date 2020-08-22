import math
import queue

h, w = map(int, input().split(" "))
cy, cx = map(lambda x: int(x) - 1, input().split(" "))
dy, dx = map(lambda x: int(x) - 1, input().split(" "))
_map = [list(input()) for _ in range(h)]

for i in range(h):
    for j in range(w):
        if _map[i][j] == ".":
            _map[i][j] = i * w + j
for y in range(h):
    for x in range(w):
        area_id = _map[y][x]
        print(area_id, y * w + x)
        if area_id != y * w + x:
            continue
        q = queue.Queue()
        q.put([y, x])
        while q.qsize() != 0:
            ny, nx = q.get()
            for sx, sy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                if sx + nx < 0 or sx + nx >= w or sy + ny < 0 or sy + ny >= h:
                    continue
                if _map[sy + ny][sx + nx] == area_id or _map[sy +
                                                             ny][sx +
                                                                 nx] == "#":
                    continue
                _map[sy + ny][sx + nx] = area_id
                q.put([sy + ny, sx + nx])

print(*_map, sep="\n")

# q = queue.Queue()
# q.put([cx, cy])

# while True:
#     nx, ny = q.get()

# rstep = False
# for sx, sy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
#     nsx = nx + sx
#     nsy = ny + sy
#     if nsx < 0 or nsx >= w or nsy < 0 or nsy >= h:
#         continue
#     if _map[nsx][nsy] == "." and visited[nsx][nsy] < visited[nx][ny]:
#         rstep = True
#         visited[nsx][nsy]
#         q.put([nsx, nsy])
# if rstep:
#     for sx, sy in [[]]

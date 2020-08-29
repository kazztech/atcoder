import sys
from collections import deque

H, W = map(int, sys.stdin.readline().split())
cy, cx = map(int, sys.stdin.readline().split())
gy, gx = map(int, sys.stdin.readline().split())
cy -= 1
cx -= 1
gy -= 1
gx -= 1
grid = []
for _ in range(H):
    grid.append(sys.stdin.readline().strip())
q = deque()
q.append((cx, cy, 0))
visited_d = {}
visited_e = {}
ans = float("inf")
while q:
    x, y, e = q.popleft()
    if (x, y) in visited_e and visited_e[(x, y)] <= e:
        continue
    visited_e[(x, y)] = e
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx = x + dx
        ny = y + dy
        if 0 <= nx < W and 0 <= ny < H and grid[ny][nx] != "#":
            if nx == gx and ny == gy:
                ans = min(ans, e)
                continue
            if (nx, ny) not in visited_e:
                q.appendleft((nx, ny, e))
    for dx in range(-2, 3):
        for dy in range(-2, 3):
            if abs(dx) == 1 and dy == 0 or abs(dy) == 1 and dx == 0:
                continue
            nx = x + dx
            ny = y + dy
            if 0 <= nx < W and 0 <= ny < H and grid[ny][nx] != "#":
                if nx == gx and ny == gy:
                    ans = min(ans, e + 1)
                    continue
                if (nx, ny) not in visited_e:
                    q.append((nx, ny, e + 1))
print(-1 if ans == float("inf") else ans)

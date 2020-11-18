import math, queue

h, w = map(int, input().split(" "))
li = [list(input()) for _ in range(h)]

mvd = [[0 for _ in range(w)] for _ in range(h)]

q = queue.Queue()
q.put([0, 0])

ans = 0
while q.qsize() != 0:
    x, y = q.get()
    print(x, y, ans)
    for xscope in range(1, w - x):
        if li[y][x + xscope] == ".":
            q.put([x + xscope, y])
            mvd[y][x + xscope] = mvd[y][x] + 1
            continue
        break
    for yscope in range(1, h - y):
        if li[y + yscope][x] == ".":
            q.put([x, y + yscope])
            mvd[y + yscope][x] = mvd[y][x] + 1
            continue
        break
print(ans, mvd)
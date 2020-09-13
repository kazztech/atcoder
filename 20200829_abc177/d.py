import math
import queue

n, m = map(int, input().split(" "))
abL = [list(map(int, input().split(" "))) for _ in range(m)]
visited = [False for _ in range(n + 1)]

d = {}

for a, b in abL:
    if a in d:
        d[a].add(b)
    else:
        d[a] = set([b])

    if b in d:
        d[b].add(a)
    else:
        d[b] = set([a])

ans = 1
for k, v in d.items():
    if not visited[k]:
        cnt = 0
        q = queue.Queue()
        q.put(k)
        while q.qsize() != 0:
            ss = q.get()
            visited[ss] = True
            cnt += 1
            if cnt >= n:
                break
            for dd in list(d[ss]):
                if not visited[dd]:
                    q.put(dd)
        ans = max(ans, cnt)

print(ans)
import math
import sys

sys.setrecursionlimit(200005)

n, q = map(int, input().split(" "))
abL = [list(map(int, input().split(" "))) for _ in range(n - 1)]
pxL = [list(map(int, input().split(" "))) for _ in range(q)]

to = [[] for _ in range(200005)]
ans = [0 for _ in range(n + 1)]


def dfs(v, p=-1):
    for u in to[v]:
        if u == p:
            continue
        ans[u] += ans[v]
        dfs(u, v)


for a, b in abL:
    a -= 1
    b -= 1
    to[a].append(b)
    to[b].append(a)

print(to[:10])

for p, x in pxL:
    p -= 1
    ans[p] += x

dfs(0)

print(ans)

for a in ans[:n]:
    print(a)
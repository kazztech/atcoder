import math
from queue import Queue

n, m = map(int, input().split(" "))

gh = {}
for i in range(m):
    p1, p2 = map(int, input().split(" "))
    if p1 in gh:
        gh[p1].append(p2)
    else:
        gh[p1] = [p2]

    if p2 in gh:
        gh[p2].append(p1)
    else:
        gh[p2] = [p1]

_mp = [-1 for _ in range(n)]
_mp[0] = 0
q = Queue()
q.put(1)

while q.qsize() != 0:
    cp = q.get()
    for p in gh[cp]:
        if _mp[p - 1] != -1: continue
        q.put(p)
        _mp[p - 1] = cp

for k, v in gh.items():
    if len(v) == 0:
        print("No")
        exit()

print("Yes")
for mpi in _mp[1:]:
    print(mpi)

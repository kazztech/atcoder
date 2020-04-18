import math
from collections import deque
import copy

n = int(input())
pL = list(input().split(" "))
qL = list(input().split(" "))

q = deque()
li = list(map(str, range(1, n + 1)))

for i in range(1, n + 1):
    q.append(str(i))

while True:
    item = q.popleft()
    if len(item) == n:
        q.appendleft(item)
        break
    for s in li:
        if not s in list(item):
            q.append(item + s)

idx = 1
pi, qi = 0, 0
while len(q) != 0:
    item = q.popleft()
    if item == "".join(pL):
        pi = idx
    if item == "".join(qL):
        qi = idx
    idx += 1

print(abs(qi - pi))
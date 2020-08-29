import math

n = int(input())
aL = list(map(int, input().split(" ")))

l = []
r = []
for i in range(n):
    if i % 2 == 0:
        l.append(aL[i])
    else:
        r.append(aL[i])

if n % 2 == 0:
    print(*list(reversed([*reversed(l), *r])))
else:
    print(*reversed(l), *r)

import math

n = int(input())
aL = list(map(int, input().split(" ")))

crnt = 1
for a in aL:
    if a == crnt:
        crnt += 1

if crnt == 1:
    print(-1)
else:
    print(n - (crnt - 1))
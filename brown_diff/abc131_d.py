import math

n = int(input())
ab = [list(map(int, input().split(" "))) for _ in range(n)]
ab.sort(key=lambda x: (x[1], x[0]))

jt = 0
for a, b in ab:
    jt += a
    if b < jt:
        print("No")
        exit()

print("Yes")
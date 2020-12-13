import math

n, m, t = map(int, input().split(" "))
abL = [list(map(int, input().split(" "))) for _ in range(m)]

life = n
pos = 0
for a, b in abL:
    life -= a - pos
    life = min(n, life)
    if life <= 0:
        print("No")
        exit()
    pos = b
    life += b - a
    life = min(n, life)

life -= t - pos
life = min(n, life)

if life <= 0:
    print("No")
else:
    print("Yes")

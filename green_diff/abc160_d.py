import math

n, x, y = list(map(int, input().split(" ")))

li2 = [[0 for _ in range(n)] for _ in range(n)]

for s in range(n - 1):
    for e in range(s + 1, n):
        li2[e][s] = min(abs(e - s),
                        abs(y - s) + 1 + abs(e - x),
                        abs(x - s) + 1 + abs(e - y))

li3 = [0 for _ in range(n + 1)]
for mli in li2:
    for i in mli:
        li3[i] += 1

for i in range(1, n):
    print(li3[i])

# distL = [0 for _ in range(2001)]
# for s in range(1, n + 1):
#     for e in range(s + 1, n + 1):
#         _min = 0
#         if s <= x and y <= e:
#             _min = min(e - s, (e - y) + (x - s) + 1)
#         elif s > x and y <= e:
#             _min = min(s - x + 1, e - s)
#         elif s <= x and y > e:
#             _min = min(e - s, (x - s) + (y - e) + 1)
#         else:
#             _min = min((s - x) + (y - e) + 1, e - s)
#         distL[_min] += 1

# for i in range(1, n):
#     print(distL[i])
import math

n, k = map(int, input().split(" "))

abL = []
for i in range(n):
    abL.append(list(map(int, input().split(" "))))

abL = sorted(abL, key=lambda x: x[0])

cnt = 0
for a, b in abL:
    cnt += b
    if cnt >= k:
        print(a)
        exit()

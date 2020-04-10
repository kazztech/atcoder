import math

n, k = map(int, input().split(" "))
hLi = list(map(int, input().split(" ")))

cnt = 0

for h in hLi:
    if h >= k:
        cnt += 1

print(cnt)
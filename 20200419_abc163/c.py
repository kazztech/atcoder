import math

n = int(input())
aL = list(map(int, input().split(" ")))

cnt = [0 for _ in range(n)]
cnt[0] = 1

for i in range(1, n - 1):
    cnt[aL[i] - 1] += 1

for c in cnt:
    print(c)
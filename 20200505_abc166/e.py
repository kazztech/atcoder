import math

n = int(input())
aL = list(map(int, input().split(" ")))

ans = 0
for i in range(n):
    for j in range(i, n):
        print(j - aL[j], aL[i] - i)
        if j - i == aL[i] + aL[j]:
            ans += 1

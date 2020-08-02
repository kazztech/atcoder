import math

k, s = map(int, input().split(" "))

ans = 0
for i in range(0, k + 1):
    for j in range(0, k + 1):
        if s - i - j <= k and s - i - j >= 0:
            ans += 1

print(ans)
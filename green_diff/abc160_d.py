import math

n, x, y = map(int, input().split(" "))

ans = [0 for _ in range(n)]
for i in range(1, n):
    for j in range(i + 1, n + 1):
        ans[min(j - i, abs(i - x) + abs(j - y) + 1)] += 1

print(*ans[1:])
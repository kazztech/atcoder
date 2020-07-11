import math

n = int(input())


def f(x, y, z):
    return (x**2) + (y**2) + (z**2) + (x * y) + (y * z) + (z * x)


dp = [0 for _ in range(60001)]
C = 100  # sqrt(1000) <
for i in range(1, C):
    for j in range(1, C):
        for k in range(1, C):
            dp[f(i, j, k)] += 1

print(*dp[1:n + 1])

import math

k = int(input())
mp = [[-1] * k for _ in range(k)]


def gcd(a, b):
    if b == 0:
        return a
    if mp[a - 1][b - 1] == -1:
        mp[a - 1][b - 1] = gcd(b, a % b)
        return mp[a - 1][b - 1]
    return mp[a - 1][b - 1]


ans = 0

for i in range(1, k + 1):
    for j in range(1, k + 1):
        for k in range(1, k + 1):
            ans += gcd(k, gcd(j, i))

print(ans)
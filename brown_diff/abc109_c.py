import math

n, x = map(int, input().split(" "))
xL = sorted(list(map(int, input().split(" "))) + [x])

diff = [0 for _ in range(n)]
for i in range(n):
    diff[i] = xL[i + 1] - xL[i]

ans = diff[0]
for d in diff:
    ans = math.gcd(ans, d)

print(ans)
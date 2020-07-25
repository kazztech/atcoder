import math

n, k = map(int, input().split(" "))
hs = sorted([int(input()) for _ in range(n)], reverse=True)

ans = 10000000000000
for i in range(n - k + 1):
    j = i + k - 1
    ans = min(hs[i] - hs[j], ans)

print(ans)
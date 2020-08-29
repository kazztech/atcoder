import math

n = int(input())
aL = list(map(int, input().split(" ")))

MOD = 10**9 + 7

aL2 = [aL[-1]]
for a in reversed(aL[:-1]):
    aL2.append((aL2[-1] + a) % MOD)
aL2 = list(reversed(aL2))

ans = 0
for i in range(n - 1):
    ans += aL[i] * aL2[i + 1]
    ans %= MOD

print(ans)
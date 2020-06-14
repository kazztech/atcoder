n, k = map(int, input().split(" "))

MOD = (10**9) + 7


def dSum(s, e):
    s -= 1
    _s = s * (s + 1) // 2
    _e = e * (e + 1) // 2
    return _e - _s


ans = 0
for i in range(k, n + 1):
    # _sum = dSum(n - i - 1, n) - dSum(0, i - 1) + 1
    ans += dSum(i, n) - dSum(0, n - i) + 1

print((ans + 1) % MOD)

from functools import reduce

n, a, b = map(int, input().split(" "))

MOD = 10**9 + 7


def comb(n, r, mod=float("inf")):
    c = 1
    m = 1
    r = min(n - r, r)
    for i in range(r):
        c = c * (n - i) % mod
        m = m * (i + 1) % mod
    return c * pow(m, mod - 2, mod) % mod


print((pow(2, n, MOD) - comb(n, a, MOD) - comb(n, b, MOD) - 1) % MOD)

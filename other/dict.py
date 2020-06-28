def comb(n, r, mod=float("inf")):
    c = 1
    m = 1
    r = min(n - r, r)
    for i in range(r):
        c = c * (n - i) % mod
        m = m * (i + 1) % mod
    return c * pow(m, mod - 2, mod) % mod


def pow2(n):
    if n == 0: return 1
    x = pow2(n // 2)
    x *= x
    if n % 2 == 1: x *= 2
    return x


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


print(pow2(1000_000_000) % 1000000007)

def choose(n, a):
    x = 1
    y = 1
    for i in range(a):
        x *= n - 1
        y *= i + 1
    return x // y


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

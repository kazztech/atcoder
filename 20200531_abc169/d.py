import math

n = int(input())


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


primes = prime_factorize(n)

d = {}
for p in primes:
    if p in d:
        d[p] += 1
    else:
        d[p] = 1

ans = 0
for k, v in d.items():
    wp = 2
    d[k] -= 1
    ans += 1
    if wp == 2 and d[k] == 1:
        d[k] = 0
        continue
    while d[k] != 0:
        if wp * 2 + 1 <= d[k]:
            d[k] -= wp
            wp += 1
            ans += 1
        else:
            d[k] = 0
            ans += 1

print(ans)
import math

n = int(input())

MOD = 1_000_000_007


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


if n == 1:
    print(0)
elif n == 2:
    print(2)
else:
    print(prime_factorize(974))
    # ans = 0
    # for i in range(1000):
    #     li = list(str(i).zfill(3))
    #     if "0" in li and "9" in li:
    #         ans += 1
    #         print(li)

    # print(ans)
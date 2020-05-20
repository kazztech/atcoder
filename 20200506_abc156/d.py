import math

MOD = 1000000007

n, a, b = map(int, input().split(" "))


def choose(n, a):
    ret = 1
    for i in range(a):
        ret *= n - i
        ret %= MOD
        ret *= i + 1
        ret %= MOD
    return ret


def pow2(num):
    c = 2
    d = 1
    dic = {d: c}

    for _ in range(20):
        c **= 2
        d *= 2
        dic[d] = c

    ret = 0
    while d != 0:
        if num >= d:
            num -= d
            if ret == 0:
                ret = dic[d] % MOD
            else:
                ret *= dic[d] % MOD
        else:
            d //= 2
    return ret


print((pow(2, n, MOD) - choose(n, a) - choose(n, b) - 1) % MOD)

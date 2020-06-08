import math


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


l, r = map(int, input().split(" "))

_min = float("inf")
for i in range(l, r + 1):
    for j in range(i + 1, r + 1):
        v = (i * j) % 2019
        # どっちかに2019の倍数が来るのは最大2019**2だから
        if v == 0:
            print(0)
            exit()
        else:
            _min = min(_min, v)

        #print(i, j, (i * j) % 2019)
        #print(prime_factorize(i), prime_factorize(j))
print(_min)

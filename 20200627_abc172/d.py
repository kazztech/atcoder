import math


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return len(divisors)


n = int(input())
_sum = 0
li = [0 for _ in range(10000001)]
for i in range(1, n + 1):
    print(make_divisors(i), i)
    #_sum += make_divisors(i) * i

print(_sum)
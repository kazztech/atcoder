import math
from operator import mul
from functools import reduce

l = int(input())


def cmb(n, r):
    r = min(n - r, r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


a = cmb(l - 1, 11)
print(a)
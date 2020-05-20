from fractions import gcd

a, b, c, d = map(int, input().split(" "))


def lcm(x, y):
    return (x * y) // gcd(x, y)


def sj(base, i1, i2):
    cz = base // i1
    dz = base // i2
    cd = base // lcm(i1, i2)
    return base - (cz + dz - cd)


print(sj(b, c, d) - sj(a - 1, c, d))

import math

n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

bn = min([a, b, c, d, e])

print(((n - 1) // bn) + 5)
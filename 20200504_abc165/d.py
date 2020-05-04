import math

a, b, n = map(int, input().split(" "))

k = min(n, b - 1)
print(math.floor(a * k / b) - a * math.floor(k / b))
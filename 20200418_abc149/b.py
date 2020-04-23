import math

a, b, k = map(int, input().split(" "))

if a < k:
    print(0, max(0, b - abs(a - k)))
    exit()

if a >= k:
    print(a - k, b)
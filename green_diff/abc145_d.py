import math

x, y = map(int, input().split(" "))

if (x / y > 2 or y / x > 2) or (x + y) % 3 != 0:
    print(0)
    exit()

layer = (x + y) // 3
print(layer)

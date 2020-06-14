import math

n = int(input())

v = math.floor(math.sqrt(n))
while True:
    if n % v == 0:
        print(v + (n // v) - 2)
        exit()
    v -= 1
import math

a, b = map(int, input().split(" "))

for i in range(1, 10000):
    if math.floor(i * 0.08) == a and math.floor(i * 0.1) == b:
        if math.floor(i * 0.08) != 0:
            print(i)
            exit()

print(-1)
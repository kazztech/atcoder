import math

n = int(input())
spL = [input().split(" ") + [i + 1] for i in range(n)]

for restaurant in sorted(spL, key=lambda x: (x[0], 1000000 - int(x[1]))):
    print(restaurant[2])
import math

i = int(input())

if i % 1000 == 0:
    print(0)
    exit()

print(1000 - (i % 1000))

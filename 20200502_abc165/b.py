import math

x = int(input())
p = 100

i = 1
while True:
    p = math.floor(p * 1.01)
    if p >= x:
        print(i)
        exit()
    i += 1
import math

x = int(input())

fL = [i**5 for i in range(0, 1001)]

for i, f1 in enumerate(fL):
    for j, f2 in enumerate(fL):
        a = j
        b = i
        if f1 + f2 == x:
            print(a, -b)
            exit()
        if f1 - f2 == x:
            print(b, a)
            exit()

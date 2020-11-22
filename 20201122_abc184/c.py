import math

r1, c1 = map(int, input().split(" "))
r2, c2 = map(int, input().split(" "))

if r1 == r2 and c1 == c2:
    print(0)
    exit()

if r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(c1 - c2) + abs(r1 -
                                                                  r2) <= 3:
    print(1)
    exit()

if abs(r1 - c1) + abs(r2 - c2) % 2 == 0:
    print(2)
    exit()

b1 = c1 - r1
b2 = c2 + r2
x = abs(b1 - b2) // 2
y = (abs(b1 - b2) // 2) + b1
if (abs(c1 - y) + abs(r1 - x) <= 3) or (abs(y - c2) + abs(x - r2) <= 3):
    print(2)
else:
    print(3)

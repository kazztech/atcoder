import math

a, b, x = map(int, input().split(" "))

cap = a * a * b

h = (x / cap) * b
if h / b >= 0.5:
    gap = b - h
    print(math.degrees(math.atan((gap / (a / 2)))))
else:
    vol = h * a
    gap = (vol / b) * 2
    print(math.degrees(math.atan(b / gap)))
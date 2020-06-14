import math

a, b, x = map(int, input().split(" "))

left = 0
right = 1000000000

if a * right + b * len(str(right)) < x:
    print(right)
    exit()

while True:
    if right - left <= 1:
        break
    middle = ((right - left) // 2) + left
    c = a * middle + b * len(str(middle))
    if x > c:
        left = middle
    else:
        right = middle

if left == 0:
    print(0)
    exit()

while True:
    c = a * left + b * len(str(left))
    if c > x:
        print(left - 1)
        exit()
    left += 1
import math

n, k = map(int, input().split(" "))
aL = list(map(int, input().split(" ")))

left = 0
right = 100
mid = right // 2

for i in range(50):
    cut = 0
    for a in aL:
        cut = math.ceil(a / mid) - 1
    print(i, cut)
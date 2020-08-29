import math

n = int(input())
aL = list(map(int, input().split(" ")))

mc = 0
for a in aL:
    if a < 0:
        mc += 1

aL = list(map(lambda x: abs(x), aL))

if mc % 2 == 0:
    print(sum(aL))
else:
    print(sum(aL) - (2 * min(aL)))

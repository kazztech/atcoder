import math

n = int(input())
aL = list(map(int, input().split(" ")))
bL = list(map(int, input().split(" ")))

aSum = sum(aL)

for i in range(n):
    dmg1 = min(aL[i], bL[i])
    aL[i] -= dmg1
    bL[i] -= dmg1

    dmg2 = min(aL[i + 1], bL[i])
    aL[i + 1] -= dmg2
    bL[i] -= dmg2

print(aSum - sum(aL))

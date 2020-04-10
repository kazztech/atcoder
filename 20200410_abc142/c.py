import math

n = int(input())
aLi = list(map(int, input().split(" ")))
sLi = list(range(n))

for i, a in enumerate(aLi):
    sLi[a - 1] = str(i + 1)

print(" ".join(sLi))

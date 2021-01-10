import math

i = int(input())
aL = list(map(int, input().split(" ")))
bL = list(map(int, input().split(" ")))

sm = 0
for n in range(i):
    sm += aL[n] * bL[n]

if sm == 0:
    print("Yes")
else:
    print("No")
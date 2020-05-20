import math

n, k = map(int, input().split(" "))
aL = list(map(int, input().split(" ")))
l = [False for _ in range(n)]

crnt = 0
c = 0
c2 = 0
while True:
    if l[crnt]:
        syuki = c
        c2 = 0
        while True:
            if aL[crnt] == aL[c - c2]:
                break
            c2 += 1

        break
    l[crnt] = True
    crnt = aL[crnt] - 1
    c += 1

syuki = c2 + 1
start = c - c2

k -= start + 1
crnt = aL[start]

print(syuki)

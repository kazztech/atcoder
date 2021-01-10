import math

n = int(input())
sL = [input() for _ in range(n)]

for i, s in enumerate(sL):
    if s[0] == "!":
        sL[i] = s[1:]

print(sL)
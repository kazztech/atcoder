import math

n = int(input())
cL = input()

ans = 0
s = 0
e = n - 1
while True:
    if s >= e:
        break
    if cL[s] == "R":
        s += 1
        continue
    else:
        if cL[e] == "W":
            e -= 1
            continue
        else:
            ans += 1
            s += 1
            e -= 1

print(ans)
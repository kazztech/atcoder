import math

s = input()
li = [0 for _ in range(len(s))]

for i in range(len(s)):
    if s[i] == "R":
        t = s[i:].index("L")
        if t % 2 != 0:
            li[i + t - 1] += 1
        else:
            li[i + t] += 1
    else:
        t = s[:i].rfind("R")
        if (i - t) % 2 != 0:
            li[t + 1] += 1
        else:
            li[t] += 1

print(*li)


import math

s = input()
t = input()

ans = len(t)
for i in range(len(s) - len(t) + 1):
    c = 0
    for j in range(len(t)):
        if s[i + j] != t[j]:
            c += 1
    ans = min(ans, c)

print(ans)
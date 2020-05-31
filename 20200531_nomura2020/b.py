import math

s = list(input()[::-1])

for i in range(len(s)):
    if s[i] == "?":
        s[i] = "D"

print("".join(s[::-1]))
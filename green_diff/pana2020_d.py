import math

n = int(input())

x = ["a"]
alps = "abcdefghijk"
i = 1
while i < n:
    y = []
    for t in x:
        for s in alps[:len(set(t)) + 1]:
            y.append(t + s)
    x = y
    i += 1

print("\n".join(x))

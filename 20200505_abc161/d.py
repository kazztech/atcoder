import math

k = int(input())

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

c = 0
while k > len(l):
    f = l[c] - (l[c] // 10 * 10)
    if f != 0:
        l.append(l[c] * 10 + f - 1)
    l.append(l[c] * 10 + f)
    if f != 9:
        l.append(l[c] * 10 + f + 1)
    c += 1

print(l[k - 1])

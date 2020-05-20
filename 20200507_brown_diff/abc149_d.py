import math

n, k = map(int, input().split(" "))
r, s, p = map(int, input().split(" "))
t = input()

w = {"r": p, "s": r, "p": s}

li = [0 for _ in range(n)]
for i in range(len(t)):
    wp = w[t[i]]
    if not (i - k >= 0 and li[i - k] == wp and t[i] == t[i - k]):
        li[i] = wp

print(sum(li))
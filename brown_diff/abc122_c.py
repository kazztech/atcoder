import math

n, q = map(int, input().split(" "))
s = input()

lrL = [list(map(int, input().split(" "))) for _ in range(q)]

li = [0] * n
mx = 0
for i in range(n - 1):
    if s[i] == "A" and s[i + 1] == "C":
        mx += 1
    li[i + 1] = mx

for l, r in lrL:
    print(li[r - 1] - li[l - 1])

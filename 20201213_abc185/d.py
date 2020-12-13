import math

n, m = map(int, input().split(" "))

if m == 0:
    print(1)
    exit()

li = list(map(int, input().split(" ")))
li = sorted(li)

ap = []
if li[0] != 1:
    ap.append(li[0] - 1)
for i in range(1, m):
    if (li[i] - li[i - 1] - 1) > 0:
        ap.append(li[i] - li[i - 1] - 1)

if li[-1] != n:
    ap.append(n - li[-1])

if len(ap) == 0:
    print(0)
    exit()
mi = min(ap)
ans = 0
for a in ap:
    if a == 0:
        continue
    ans += math.ceil(a / mi)
print(ans)
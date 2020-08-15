import math

n, k = map(int, input().split(" "))
pL = list(map(int, input().split(" ")))
cL = list(map(int, input().split(" ")))

if len(list(filter(lambda x: x > 0, cL))) == 0:
    print(max(cL))
    exit()

ans = 0
for i in range(n):
    sm = []
    crnt = pL[i]
    for _ in range(min(k, n)):
        if pL[i] == crnt - 1:
            break
        sm.append(cL[crnt - 1])
        crnt = pL[crnt - 1]
    t = sum(sm)

    a = 0
    if t >= 0:
        a = t * (k // n)

    mi = 0
    s = 0
    for j in range(len(sm)):
        s += sm[j]
        mi = max(mi, s)

    ans = max(ans, mi + a)

print(ans)
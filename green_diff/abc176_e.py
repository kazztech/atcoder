import math

h, w, m = map(int, input().split(" "))
hwL = [list(map(int, input().split(" "))) for _ in range(m)]

lh = [0 for _ in range(300005)]
lw = [0 for _ in range(300005)]

sh = set()
sw = set()

for h, w in hwL:
    lh[h] += 1
    lw[w] += 1
    sh.add(h)
    sw.add(w)

hmax = max(lh)
wmax = max(lw)
ans = hmax + wmax - 1

for h in sh:
    if lh[h] == hmax:
        for w in sw:
            if lw[w] == wmax:
                for h2, w2 in hwL:
                    print(h, w, h2, w2)
                    if h == h2 and w != w2:
                        print(ans)
                        exit()

print(ans - 1)

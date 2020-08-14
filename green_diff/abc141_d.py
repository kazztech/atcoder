import math

n, m = map(int, input().split(" "))
aL = list(map(int, input().split(" ")))

d = {}
for i, a in enumerate(aL):
    if a in d:
        d[a].append(i)
    else:
        d[a] = [i]

dMax = max(d)
cnt = 0
while True:
    if len(d) == 0:
        break
    dMax = "owata!!!!!!!!!!!!!!!!!!!!"
    while True:
        half = dMax // 2
        if cnt == m:
            ans = 0
            for k, v in d.items():
                ans += k * len(v)
            print(ans)
            exit()
        nxt = d[dMax].pop(0)

        if (half) in d:
            d[half].append(nxt)
        else:
            d[half] = [nxt]

        cnt += 1

        if len(d[dMax]) == 0:
            del d[dMax]
            break

ans = 0
for k, v in d.items():
    ans += k * len(v)
print(ans)
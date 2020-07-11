n, k = map(int, input().split(" "))
aL = list(map(int, input().split(" ")))

ans = 0
sSum = 0
last = 0

for a in aL:
    if a >= k: ans += 1

for s in range(n):
    sSum = aL[s]
    for e in range(max(last, s + 1), n):
        sSum += aL[e]
        if sSum >= k:
            ans += n - e
            last = e - 1
            break

print(ans)
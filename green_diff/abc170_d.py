n = int(input())
aL = sorted(list(map(int, input().split(" "))))
# aL = sorted(list(set(aLP)))

dp = [False for _ in range(1000001)]

d = {}
for a in aL:
    if a in d:
        d[a] += 1
    else:
        d[a] = 1

ans = 0
for a in aL:
    if dp[a]:
        continue
    if d[a] > 1:
        c = 1
        while a * c <= 1000000:
            dp[a * c] = True
            c += 1
        continue
    ans += 1

    c = 1
    while a * c <= 1000000:
        dp[a * c] = True
        c += 1

print(ans)

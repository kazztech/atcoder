n, k = map(int, input().split())
aL = list(map(int, input().split()))

ans = 0
cnt = 0
r = 0

for l in range(n):
    while cnt < k:
        if r == n:
            break
        cnt += aL[r]
        r += 1
    if cnt < k:
        break
    ans += n - r + 1
    cnt -= aL[l]
print(ans)

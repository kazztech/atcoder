import math

n = int(input())
aL = list(map(int, input().split(" ")))

dp = [0] * (n + 1)

for index, i in enumerate(aL):
    dp[index + 1] = dp[index] + i

ans = -1000000000
cnt = 0
max_index = 0
for i, d in enumerate(dp):
    cnt += d
    if ans < cnt:
        ans = cnt
        max_index = i

acnt = 0
aans = -1000000000
for a in aL:
    acnt += a
    aans = max(aans, acnt)

if aans >= dp[max_index] and max_index == n:
    print(max(0, ans - dp[max_index] + aans))
else:
    print(max(0, ans + aans))
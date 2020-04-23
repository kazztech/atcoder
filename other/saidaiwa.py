aL = list(map(int, input().split(" ")))

dp = [0 for _ in range(len(aL))]

dp[0] = aL[0]
for i in range(1, len(aL)):
    if dp[i - 1] < dp[i - 1] + aL[i]:
        dp[i] = dp[i - 1] + aL[i]
    else:
        dp[i] = dp[i - 1]

print(dp[len(aL) - 1])
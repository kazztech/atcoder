import math
import queue

n, m = map(int, input().split(" "))
aL = [int(input()) for _ in range(m)]

dp = [-1] * (n + 1)
dp[0] = 1

for a in aL:
    dp[a] = 0

for i in range(1, n + 1):
    if dp[i] == 0:
        continue
    if i == 1:
        dp[i] = dp[i - 1]
    else:
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1_000_000_007

print(dp[n] % 1_000_000_007)

# q = queue.Queue()
# q.put(0)

# cnt = 0
# while not q.empty():
#     c = q.get()
#     if dp[c] != -1:
#         cnt += dp[c]
#         continue
#     if c == n:
#         cnt += 1
#         continue
#     q.put(c + 1)
#     if c + 1 != n:
#         q.put(c + 2)
#     dp[c] = cnt

# def ppp(num):
#     cnt = 0
#     q = queue.Queue()
#     q.put(num)
#     while not q.empty():
#         c = q.get()
#         if dp[c] != -1:
#             cnt += dp[c]
#             continue
#         if c == num:
#             cnt += 1
#             continue
#         q.put(c + 1)
#         if c + 1 != num:
#             q.put(c + 2)
#         dp[c] = cnt
#     print(cnt)
#     return cnt

# cli = [aL[0] - 1]
# for i in range(1, m):
#     if abs(aL[i] - aL[i - 1]) == 1:
#         print(0)
#         exit()
#     cli.append(aL[i] - aL[i - 1] - 1)
# cli.append(n - aL[-1] - 1)

# ans = 1
# for c in cli:
#     ans = (ans * ppp(c)) % 1_000_000_007

# print(ans)

# dp = [-1] * (n + 1)
# def od(num):
#     if dp[num] != -1:
#         return dp[num]
#     q = queue.Queue()
#     q.put(num)
#     cnt = 0
#     while not q.empty():
#         c = q.get()
#         if c == 0:
#             cnt += 1
#             continue
#         if c != 1:
#             q.put(c - 2)
#         q.put(c - 1)
#     dp[num] = cnt
#     return cnt
# if m == 0:
#     print(od(n))
#     exit()
# cli = [aL[0] - 1]
# for i in range(1, m):
#     if abs(aL[i] - aL[i - 1]) == 1:
#         print(0)
#         exit()
#     cli.append(aL[i] - aL[i - 1] - 1)
# cli.append(n - aL[-1] - 1)
# print(cli)
# ans = 1
# for c in cli:
#     ans = (ans * od(c)) % 1_000_000_007
# print(ans % 1_000_000_007)
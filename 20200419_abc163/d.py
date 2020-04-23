import math

n, k = map(int, input().split(" "))

w = list(range(n + 1))
a = [0 for _ in range(n)]

mx = sum(w[(n // 2) + 1:]) - sum(w[:(n // 2) + 1]) + 1
a[(n // 2)] = mx

cnt = 1
prev = mx
for i in range((n // 2) - 1, -1, -1):
    a[i] = prev - cnt
    a[n - i - 1] = prev - cnt
    cnt += 2
    prev = a[i]

print((sum(a[k - 1:]) + 1) % 1000000007)

# w = list(range(n + 1))
# a = []

# sm = 0
# for i in range(k - 1, n):
#     i = i + 1
#     sm += sum(w[n - i + 1:]) - sum(w[0:i]) + 1

# print(sm + 1)

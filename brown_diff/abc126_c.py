import math

n, k = map(int, input().split(" "))

# ans = (1 / n) * (1 / 2)**math.floor(math.log(k, 2) + 1)

# for i in range(2, n + 1):
#     d = math.floor(math.log(k, i))
#     ans += (1 / n) * (1 / 2)**d

ans = 0

for i in range(1, n + 1):
    v = i
    c = 0
    while True:
        if v >= k:
            ans += (1 / n) * (1 / 2)**c
            break
        v *= 2
        c += 1

print(ans)
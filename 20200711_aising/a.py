import math

l, r, d = map(int, input().split(" "))

ans = 0
for i in range(l, r + 1):
    print(i)
    if i % d == 0:
        ans += 1

print(ans)
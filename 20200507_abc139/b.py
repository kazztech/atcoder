import math

a, b = map(int, input().split(" "))

c = 1

ans = 0
while True:
    if c >= b:
        break
    c += a - 1
    ans += 1

print(ans)

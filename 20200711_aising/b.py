import math

n = int(input())
aL = list(map(int, input().split(" ")))

ans = 0
for index, a in enumerate(aL):
    if index % 2 == 1 and a % 2 == 1:
        ans += 1

print(ans)

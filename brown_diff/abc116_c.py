import math

n = int(input())
hL = list(map(int, input().split(" ")))

ans = 0
for i in range(1, 101):
    r = False
    for h in hL:
        if i <= h:
            if not r:
                ans += 1
            r = True
        else:
            r = False

print(ans)
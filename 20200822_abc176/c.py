import math

n = int(input())
aL = list(map(int, input().split(" ")))

mx = aL[0]
ans = 0
for a in aL[1:]:
    if mx > a:
        ans += mx - a
    else:
        mx = a

print(ans)
import math

n = int(input())
aL = list(map(int, input().split(" ")))

ans = 2
mx = 0
for i in reversed(range(2, 1000)):
    cnt = 0
    for a in aL:
        if a % i == 0:
            cnt += 1
    if mx < cnt:
        ans = i
        mx = cnt

print(ans)
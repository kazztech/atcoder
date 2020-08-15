import math

n = int(input())
aL = sorted(list(map(int, input().split(" "))))

ans = aL[0]
for a in aL:
    ans = min(math.gcd(aL[0], a), ans)

print(ans)
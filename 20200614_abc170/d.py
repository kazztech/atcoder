import math

n = int(input())
aL = sorted(list(set(list(map(int, input().split(" "))))))

n = len(aL)
if n == 1:
    print(0)
    exit()
ans = n
for i in range(n - 1, -1, -1):
    for j in range(i):
        if aL[j] * 2 > aL[i]:
            break
        if aL[i] % aL[j] == 0:
            ans -= 1
            break

print(ans)

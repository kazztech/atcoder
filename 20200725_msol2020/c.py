import math

n, k = map(int, input().split(" "))
aL = list(map(int, input().split(" ")))

ans = 0

for i in range(1, n - k + 1):
    j = i + k - 1
    if aL[i - 1] < aL[j]:
        print("Yes")
    else:
        print("No")
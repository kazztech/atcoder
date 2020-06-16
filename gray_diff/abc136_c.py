import math

n = int(input())
li = list(map(int, input().split(" ")))

for i in range(n - 1, 0, -1):
    if li[i - 1] <= li[i]:
        continue
    li[i - 1] -= 1
    if li[i - 1] > li[i]:
        print("No")
        exit()

print("Yes")
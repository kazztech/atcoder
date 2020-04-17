import math

n, k, m = map(int, input().split(" "))
aSum = sum(list(map(int, input().split(" "))))

for i in range(k + 1):
    s = (aSum + i)
    if m * n <= s:
        print(i)
        exit()

print(-1)
import math

k = int(input())

m = 7 % k
for i in range(1, k + 1):
    if m == 0:
        print(i)
        exit()
    m = (m * 10 + 7) % k
print(-1)
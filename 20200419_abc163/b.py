import math

n, m = map(int, input().split(" "))
aL = list(map(int, input().split(" ")))

if n < sum(aL):
    print(-1)
else:
    print(n - sum(aL))
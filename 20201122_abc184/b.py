import math

n, x = map(int, input().split(" "))
s = input()

cnt = x
for si in list(s):
    if si == "x":
        cnt = max(0, cnt - 1)
    else:
        cnt += 1

print(cnt)
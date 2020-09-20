import math

n = int(input())
dL = [list(map(int, input().split(" "))) for _ in range(n)]

cnt = 0
for d in dL:
    if d[0] == d[1]:
        cnt += 1
    else:
        cnt = 0
    if cnt == 3:
        print("Yes")
        exit()

print("No")
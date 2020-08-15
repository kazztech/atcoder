import math

n = int(input())
hL = list(map(int, input().split(" ")))

ans = 0
cont = False
while True:
    if len(set(hL)) == 1 and hL[0] == 0:
        break
    cont = False
    cnt = 0
    for j in range(n):
        if hL[j] != 0:
            hL[j] -= 1
            if not cont:
                cnt += 1
            cont = True
            continue
        else:
            cont = False

    ans += cnt

print(ans)

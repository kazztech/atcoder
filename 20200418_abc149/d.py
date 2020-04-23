import math

n, k = map(int, input().split(" "))
r, s, p = map(int, input().split(" "))
t = input()


def dec(num):
    if num == 0: return num
    return num


scr = 0
rc, sc, pc = 0, 0, 0
for j in list(t):
    if j == "r":
        rc, sc, pc = dec(rc), dec(sc), dec(pc)
        rc = k
        if pc == 0:
            scr += p
            pc = k
        else:
            pass

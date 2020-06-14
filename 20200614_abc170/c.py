import math

x, n = map(int, input().split(" "))
ps = input()
if ps == "":
    print(x)
    exit()
ps = sorted(list(map(int, ps.split(" "))))

if not x in ps or len(ps) == 0:
    print(x)
    exit()

g = 1
while True:
    if not (x - g in ps):
        print(x - g)
        exit()
    if not (x + g in ps):
        print(x + g)
        exit()
    g += 1
    if g == 101:
        print(0)
        exit()

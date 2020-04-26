import math

th, ta, mh, ma = map(int, input().split(" "))

while True:
    mh -= ta
    if mh <= 0:
        print("Yes")
        exit()

    th -= ma
    if th <= 0:
        print("No")
        exit()
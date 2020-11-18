import math

sx, sy, gx, gy = map(int, input().split(" "))
print(sx + (gx - sx) * (sy / (sy + gy)))

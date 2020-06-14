import math

a, v = map(int, input().split(" "))
b, w = map(int, input().split(" "))
t = int(input())

if w >= v:
    print("NO")
    exit()

fast = abs(v - w)
dist = abs(b - a)

if fast * t >= dist:
    print("YES")
else:
    print("NO")
import math

x, y = map(int, input().split(" "))

for i in range(0, 101):
    for j in range(0, 101):
        s = i + j
        a = i * 2 + j * 4
        if s == x and y == a:
            print("Yes")
            exit()

print("No")

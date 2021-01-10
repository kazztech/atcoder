import math

n, m = map(int, input().split(" "))

if (abs(n - m) <= 2):
    print("Yes")
else:
    print("No")
import math

i = int(input())
n, m = map(int, input().split(" "))

for s in range(n, m + 1):
    if s % i == 0:
        print("OK")
        exit()

print("NG")
import math

aka, mi, ao = map(int, input().split(" "))
k = int(input())

for i in range(k):
    if mi <= aka:
        mi *= 2
        continue
    if ao <= mi:
        ao *= 2
        continue
    ao *= 2

if ao > mi > aka:
    print("Yes")
else:
    print("No")
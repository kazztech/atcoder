import math

n = list(map(int, "".join(input())))

if sum(n) % 9 == 0:
    print("Yes")
else:
    print("No")

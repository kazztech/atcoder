import math

start, kai, step = map(int, input().split(" "))

if 0 <= abs(start) - (kai * step):
    print(abs(start) - (kai * step))
    exit()

ans1 = start % step
ans2 = abs(ans1 - step)
if (kai - abs(start // step)) % 2 == 0:
    print(abs(ans1))
else:
    print(abs(ans2))

import math

n = int(input())

if n % 2 == 1:
    print(0)
    exit()

c = 2
ans = 1
for i in range(101):
    ans = ans * c
    print(c, str(ans)[-40:])
    c += 2
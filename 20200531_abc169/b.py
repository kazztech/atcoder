import math

n = int(input())
li = list(map(int, input().split(" ")))

if 0 in li:
    print(0)
    exit()

ans = li[0]
del li[0]

for i in li:
    ans *= i
    if ans > 1000000000000000000:
        print(-1)
        exit()

print(ans)
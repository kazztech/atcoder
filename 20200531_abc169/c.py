import math

a, b = map(float, input().split(" "))

b *= 100

ans = math.floor((a * b) // 100)

print(ans)
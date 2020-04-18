import math

n = int(input())
aL = list(map(int, input().split(" ")))

s = set()
for a in aL:
    if a in s:
        print("NO")
        exit()
    else:
        s.add(a)

print("YES")
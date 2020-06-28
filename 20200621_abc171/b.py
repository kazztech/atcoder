import math

n, k = map(int, input().split(" "))
pL = sorted(list(map(int, input().split(" "))))

print(sum(pL[:k]))

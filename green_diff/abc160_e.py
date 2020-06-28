import math

x, y, a, b, c = map(int, input().split(" "))
qL = sorted(list(map(int, input().split(" "))), reverse=True)[:x]
pL = sorted(list(map(int, input().split(" "))), reverse=True)[:y]
rL = sorted(list(map(int, input().split(" "))), reverse=True)

print(sum(sorted(qL + pL + rL, reverse=True)[:x + y]))

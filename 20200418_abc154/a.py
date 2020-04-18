import math

s1, s2 = input().split(" ")
a, b = map(int, input().split(" "))
c = input()

if s1 == c:
    a -= 1
if s2 == c:
    b -= 1

print(a, b)
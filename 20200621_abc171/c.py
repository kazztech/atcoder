import math

n = int(input())

su = list("abcdefghijklmnopqrstuvwxyz")

ans = ""
li = []
while True:
    if n <= 26:
        li.append(su[n - 1])
        break
    li.append(su[n % 26 - 1])
    n = n // min(n // 26, 26)
    print(n)

print("".join(reversed(li)))
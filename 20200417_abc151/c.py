import math

n, m = map(int, input().split(" "))

d = {}
for i in range(1, n + 1):
    d[i] = {"AC": False, "WA": 0}

acc, wac = 0, 0
for _ in range(m):
    q, m = input().split(" ")
    q = int(q)

    if not d[q]["AC"]:
        if m == "WA":
            d[q]["WA"] += 1
        elif m == "AC":
            d[q]["AC"] = True
            acc += 1
            wac += d[q]["WA"]

print(acc, wac)
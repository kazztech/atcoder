import math

s = input()
i = int(input())

isR = False
head = []
tail = []

for _ in range(i):
    q = input().split(" ")

    if q[0] == "1":
        isR = not isR
    else:
        if isR:
            if q[1] == "1":
                tail.append(q[2])
            else:
                head.append(q[2])
        else:
            if q[1] == "1":
                head.append(q[2])
            else:
                tail.append(q[2])

ans = "".join(head[::-1]) + s + "".join(tail)

if isR:
    print(ans[::-1])
else:
    print(ans)
import math

n = 100  #int(input())
x = "1" * 100  #input()

dp = [0 for _ in range(200001)]

for i in range(n):
    crnt = x[i]
    x = x[:i] + "1" if crnt == "0" else "0" + x[i + 1:]
    print(x[:i], x[i + 1:])

    o = 1  #"".join(x)
    # num = int(o, 2)
    # sCnt = o.count("1")

    x = x[:i] + "1" if crnt == "0" else "0" + x[i + 1:]
    #print(sCnt)

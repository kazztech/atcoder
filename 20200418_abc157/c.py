import math

n, m = map(int, input().split(" "))

ans = list([0 for _ in range(n)])

err = False
for i in range(m):
    s, c = map(int, input().split(" "))
    if s == 1 and c == 0:
        print(0)
        exit()
    elif ans[s - 1] == 0:
        ans[s - 1] = c
    elif not ans[s - 1] == c:
        err = True

if ans[0] == 0:
    ans[0] = 1

if (n == 1 and ans[0] == 0) or (n == 1 and m == 0):
    print(0)
    exit()

if err:
    print(-1)
    exit()

print("".join(map(str, ans)))
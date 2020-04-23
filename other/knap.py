n = int(input())
aL = [list(map(int, input().split(" "))) for _ in range(n)]
w = int(input())

dp = [[0 for _ in range(101)] for _ in range(101 * 2)]

for w in range(w + 1):
    for m in range(n + 1):
        
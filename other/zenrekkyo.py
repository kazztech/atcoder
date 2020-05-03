f = 2
a = 2

li = []


def dfs(i, n, p):
    if i == f:
        li.append(n)
        return
    for j in range(p, a + 1):
        dfs(i + 1, n * 10 + j, j)


if a != 1:
    for i in range(1, a + 1):
        dfs(1, i, i)
else:
    li = [[i] * a for i in range(1, f + 1)]

print(li)
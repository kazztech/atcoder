n = 100

fb = [1, 1]

for i in range(2, n):
    fb.append(fb[i - 1] + fb[i - 2])

print(fb)
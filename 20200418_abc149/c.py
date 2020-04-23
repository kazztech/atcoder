import math

ip = int(input())

if ip == 2:
    print(2)
    exit()

primes = [2]
for i in range(3, 100001, 2):
    for p in primes:
        if i % p == 0:
            break
    else:
        primes.append(i)

primes.append(100003)
primes = primes[::-1]

for i in range(len(primes)):
    if primes[i] < ip:
        print(primes[i - 1])
        exit()

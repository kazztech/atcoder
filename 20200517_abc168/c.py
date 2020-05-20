import math

a, b, h, m = map(int, input().split(" "))

print(
    math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(
        math.radians(
            min(abs(30 * h + (360 * (m / 60) / 12) - 360 *
                    (m / 60)), 360 - abs(30 * h + (360 * (m / 60) / 12) - 360 *
                                         (m / 60)))))))

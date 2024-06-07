import math
n = int(input())
for i in range(1, n):
    print(round((((17 + 12 * math.sqrt(2)) ** i) + (17 - 12 * math.sqrt(2)) ** i - 2) // 32))

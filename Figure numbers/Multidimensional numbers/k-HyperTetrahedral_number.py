import math

k = int(input())
n = int(input())
q = 1
for i in range(k):
    q *= n + i
print("Sk 3(n) =", q // math.factorial(k))
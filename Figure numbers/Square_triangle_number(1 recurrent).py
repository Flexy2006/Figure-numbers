import math
n = int(input())
numbers = [0 for i in range(n)]
numbers[0] = "1"
for i in range(1, n):
    numbers[i] = 4 * int(numbers[i - 1]) * (8 * int(numbers[i - 1]) + 1)
for i in range(n):
    print(numbers[i])
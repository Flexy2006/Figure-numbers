import math
n = int(input())
numbers = [0 for i in range(n)]
numbers[0] = "1"
numbers[1] = "36"
for i in range(2, n):
    numbers[i] = 34 * int(numbers[i - 1]) - int(numbers[i - 2]) + 2
for i in range(n):
    print(numbers[i])
import math

k = int(input())
n = int(input())
q1 = 0
for j in range(0, k - 1):
    q2 = (n * (n + 1) * ((k - j - 2) * n - (k - j) + 5) // 6)
    q1 += ((-1) ** j) * math.factorial(k - 1) * (2 **(k - j - 1)) * q2 // (math.factorial(j) * math.factorial(k - j - 1))
    print(q1)
print("Ok(n) =", q1) #Пока неверно

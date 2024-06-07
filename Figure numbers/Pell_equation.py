import math

def continued_fraction_sqrt(n):
    """
    Найти период разложения sqrt(n) в цепную дробь.
    Возвращает коэффициенты цепной дроби и длину периода.
    """
    a0 = int(math.sqrt(n))
    if a0 * a0 == n:
        return None, None  # n должно быть не квадратом
    period = []
    m = 0
    d = 1
    a = a0
    seen = {}
    
    while (m, d, a) not in seen:
        seen[(m, d, a)] = len(period)
        period.append(a)
        
        m = d * a - m
        d = (n - m * m) // d
        if d == 0:
            break
        a = (a0 + m) // d
    
    # Найти начало повторяющейся последовательности
    start = seen[(m, d, a)]
    period = period[start:]
    
    return period, len(period)

def solve_pell(n, q):
    """
    Решить уравнение Пелля x^2 - n*y^2 = 1 и вывести период в цепной дроби,
    а также первые q пар чисел Pi и Qi
    """
    # Найти период разложения sqrt(n) в цепную дробь
    period, k = continued_fraction_sqrt(n)
    
    if period is None:
        return "n должно быть не квадратом."
    
    # Найти целую часть от sqrt(n)
    a0 = int(math.sqrt(n))
    
    # Начальные значения для P и Q
    P = [a0, a0 * period[0] + 1]
    Q = [1, period[0]]
    
    # Вычислить числители и знаменатели подходящих дробей
    for i in range(2, q + 1):
        an = period[(i - 1) % k]
        P.append(an * P[-1] + P[-2])
        Q.append(an * Q[-1] + Q[-2])

    # Формируем результат
    result = f"Период разложения в цепную дробь: k = {k}\n"
    result += f"Период: {' '.join(map(str, period))}\n"
    result += f"a0 = {a0}\n\n"
    result += f"Первые {q} пар чисел Pi и Qi:\n"
    for i in range(q):
        result += f"P_{i} = {P[i]}, Q_{i} = {Q[i]}\n"
    
    # Дополнительно выводим пары (x, y) если k четное, то kt - 1, иначе 2*kt - 1, где t - натуральное
    if k % 2 == 0:
        for t in range(1, q + 1):
            index = k * t - 1
            if index < q:
                result += f"(x_{index}, y_{index}) = ({P[index]}, {Q[index]})\n"
    else:
        for t in range(1, q + 1):
            index = 2 * k * t - 1
            if index < q:
                result += f"(x_{index}, y_{index}) = ({P[index]}, {Q[index]})\n"
    
    return result

# Вводим значения n и q
n = int(input("Введите n: "))
q = int(input("Введите q: ")) 

result = solve_pell(n, q)
print(result)
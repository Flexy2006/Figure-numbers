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

def solve_pell(n, l, q):
    """
    Решить уравнение Пелля x^2 - n*y^2 = l и вывести период в цепной дроби,
    а также первые q пар чисел Pi и Qi
    """
    # Найти период разложения sqrt(n) в цепную дробь
    period, k = continued_fraction_sqrt(n)
    
    if period is None:
        return "n должно быть не квадратом."
    
    # Начальные значения для P и Q
    P = [period[0], period[0] * period[1] + 1]
    Q = [1, period[1]]
    
    # Список для хранения всех пар (x, y)
    xy_pairs = []
    
    # Проверка начальных условий
    if P[0]*P[0] - n*Q[0]*Q[0] == l:
        xy_pairs.append((P[0], Q[0]))
    if P[1]*P[1] - n*Q[1]*Q[1] == l:
        xy_pairs.append((P[1], Q[1]))
    
    # Вычислить числители и знаменатели подходящих дробей
    for t in range(2, q + 1):
        for i in range(k):
            P.append(period[i % k] * P[-1] + P[-2])
            Q.append(period[i % k] * Q[-1] + Q[-2])
            
            # Добавляем пару (x, y) в список, если она удовлетворяет уравнению Пелля
            x = P[-1]
            y = Q[-1]
            if x*x - n*y*y == l:
                xy_pairs.append((x, y))

    # Формируем результат
    result = f"Период разложения в цепную дробь: k = {k}\n"
    result += f"Период: {' '.join(map(str, period))}\n\n"
    result += f"Пары (x, y), удовлетворяющие уравнению Пелля x^2 - {n} * y^2 = {l}:\n"
    for i, pair in enumerate(xy_pairs):
        result += f"({pair[0]}, {pair[1]})\n"
    
    return result

# Вводим значения n, l и q
n = int(input("Введите n: "))
l = int(input("Введите l: "))
q = int(input("Введите q: "))

result = solve_pell(n, l, q)
print(result)

# В последовательности на n целых чисел умножить все элементы на последний
# минимальный элемент.
import random

# Генерация последовательности
n = random.randint(5,15)
l1 = [random.randint(-10,10) for i in range(n)]
print(l1)

# Обработка
l2 = [l1[i] * min(l1[:i+1]) for i in range(n)]
print(l2)

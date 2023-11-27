# Дан список A ненулевых целых чисел размера 10. Вывести значение первого из тех
# его элементов AK, которые удовлетворяют неравенству AK < A10. Если таких
# элементов нет, то вывести 0.
import random

list1 = []
for i in range(10):
    list1.append(random.randint(-10,10))
print(list1)


result = 0
for i in list1:
    if i < list1[9]:
        result = i
        break

print(result)
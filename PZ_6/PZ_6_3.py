# Дан список A размера N и целое число K (1 < K < 4, K < N ). Осуществить
# циклический сдвиг элементов списка влево на K позиций (при этом A N перейдет в
# AN-K, AN-1 — в AN-K-1, ..., A 1 — в AN-K+1 ). Допускается использовать вспомогательный
# список из 4 элементов.
import random


# Создаём список
N = random.randint(2, 10)
list1 = []
for i in range(N):
    list1.append(random.randint(-20, 20))
print("Исходный список: ", list1)


# Генерируем число K и создаём вспомогательный список.
if N <= 4:
    K = random.randint(1, N)
    supporting_list = list1[:N]
else:
    K = random.randint(1,4)
    supporting_list = list1[:4]
print("Вспомогательный список: ", supporting_list)
print("K =",K)


# Сдвигаем все элементы, кроме первых четырёх.
for index in range(K,N):
    list1[index - K] = list1[index]

# Сдвигаем оставшиеся 4 элемента.
for index in range(K):
    list1[index - K] = supporting_list[index]
print("Список со сдвигом: ", list1)
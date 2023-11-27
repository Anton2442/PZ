# Дан список размера N. Найти номера двух ближайших элементов из этого списка (то
# есть элементов с наименьшим модулем разности) и вывести эти номера в порядке
# возрастания.
import random


N = random.randint(2, 10)
list1 = []
for i in range(N):
    list1.append(random.randint(-20, 20))
print(list1)

diff = None
for index1 in range(N):
    for index2 in range(N):

        if index1 != index2:


            a = abs(list1[index1] - list1[index2])

            if (diff is None) or (a < diff):
                diff = a
                index1_min = index1
                index2_min = index2

print(index1_min, index2_min, diff)
print([list1[index1_min], list1[index2_min]].sort())
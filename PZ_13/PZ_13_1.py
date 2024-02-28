# Сгенерировать матрицу на произвольное количество элементов, в которой задается
# преобразование от предыдущего элемента к следующему на произвольное значение.
import random

n = random.randint(1,3)
N = random.randint(3,8)
M = random.randint(3,8)
matr = []
for i in range(N):
    matr.append([0]*M)

for i in range(N):
    for j in range(M):
        matr[i][j] = M*i*n + n*j

print(matr)
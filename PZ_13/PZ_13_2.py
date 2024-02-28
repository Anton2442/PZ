# В матрице найти сумму элементов первых двух строк.
import random

N = random.randint(3,5)
M = random.randint(3,5)
matr = [[0] * M for i in range(N)]

for i in range(N):
    for j in range(M):
        matr[i][j] = random.randint(1,15)

print(matr)
print(sum((sum(matr[0]), sum(matr[1]))))
# Описать функцию PowerA3(A, B), вычисляющую третью степень числа A и
# возвращающую ее в переменную B (A — входной, B — выходной параметр; оба
# параметра являются вещественными). С помощью этой функции найти третьи
# степени пяти данных чисел.

check = False
while check != True:
    try:
        num1 = float(input("Введите число (1/5): "))
        num2 = float(input("Введите число (2/5): "))
        num3 = float(input("Введите число (3/5): "))
        num4 = float(input("Введите число (4/5): "))
        num5 = float(input("Введите число (5/5): "))
        check = True
    except ValueError:
        print("Вводите только числа!")

def PowerA3(A):
    return A ** 3

num1 = PowerA3(num1)
num2 = PowerA3(num2)
num3 = PowerA3(num3)
num4 = PowerA3(num4)
num5 = PowerA3(num5)

print(num1, num2, num3, num4, num5, sep="\n")
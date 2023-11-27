# Даны положительные числа A и B (A > Б). На отрезке длины A размещено
# максимально возможное количество отрезков длины Б (без наложений). Не
# используя операции умножения и деления, найти длину незанятой части отрезка A.


check = False
while not check:
    A = input("введите длину отрезка А: ") # Ввод числа A
    try:
        while float(A) < 0:
            A = input("введите длину отрезка А: ")
        A = float(A)
        check = True
    except:
        print("Это не число!")


check = False
while not check:
    B = input("введите длину отрезка B: ") # Ввод числа B
    try:
        while float(B) < 0:
            B = input("введите длину отрезка B: ")
        B = float(B)
        check = True
    except:
        print("Это не число!")


while A>=B and B != 0:  # Вычисления
    A -= B


print("Остаток:", A) # Результат
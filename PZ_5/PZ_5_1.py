# Составить программу, в которой функция построит изображение, в котором в первой
# строке 1 звездочка, во второй - 2, в третьей -3, ..., в строке с номером m - m звездочек.


check = False

while check == False:
    m = input("Введите целое положительное число: ")
    try:
        while  not int(m) > 0:
            m = input("Введите целое положительное число: ")
        check = True
        m = int(m)
    except ValueError:
        print("Число должно быть целым!")


def asterisk_line(K):
    print('*' * K)  # Если мы этого не изучали, ниже другой вариант.
    # for i in range(0,K):
    #     print('*', end='')
    # print('')


for i in range(0, m):
    asterisk_line(i + 1)
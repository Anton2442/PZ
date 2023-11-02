# Вывести трёхзначное число справа налево.

check = False

while check == False:
    num = input("Введите трёхзначное число: ")
    try:
        while  not (int(num) // 100 < 10) or not (int(num) // 100 >= 1):
            num = input("Введите трёхзначное число: ")
        check = True
        num = int(num)
    except:
        print("Число должно быть целым!")


a = num % 10
b = (num // 10) % 10
c = num // 100

print(a, b, c, sep="")
# Дано целое число N (>0). Используя один цикл, найти сумму 1 + 1/(1!) + 1/(2!) +
# 1/(3!) + ... + 1/(N!) (выражение N! — N-факториал — обозначает произведение всех
# целых чисел от 1 до N: N! = 1-2-.. . N). Полученное число является приближенным
# значением константы e = exp(1).


check = False

while check == False:
    N = input("Введите целое положительное число: ")
    try:
        while not int(N) > 0:
            N = input("Введите целое положительное число: ")
        check = True
        N = int(N)
    except ValueError:
        print("Число должно быть целым!")


result = 1
for i in range(1, N + 1):
    summ = 1
    for a in range(1, i + 1):
        summ *= a
    print(summ)
    result += 1/summ


print("Результат:",result)
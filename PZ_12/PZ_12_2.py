# Составить генератор (yield), который переведет символы строки из верхнего
# регистра в нижний.

def str_to_lower(str1):
    for i in str1:
        yield i.lower()

str1 = input("Введите строку с сиволами верхнего регистра:\n")
str2 = "".join([i for i in str_to_lower(str1)])
print(str2)

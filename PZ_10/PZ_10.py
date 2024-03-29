# Даны имена девочек. Определить, какие из этих имен встречаются в группах на всех вторых
# курсах, какие есть только в некоторых группах и какие не встречаются ни в одной из групп.

is_21 = {'Анна', 'Мария', 'Алиса', 'Екатерина', 'Анастасия', 'София',
         'Юлия','Виктория', 'Ксения', 'Елена', 'Александра', 'Наталья',
         'Дарья', 'Полина'}
is_22 = {'Евгения', 'Алиса', 'Милана', 'Ольга', 'Варвара', 'София',
         'Наталья', 'Виктория', 'Ксения', 'Елена', 'Александра', 'Диана',
         'Алина', 'Елизавета'}
is_23 = {'Александра', 'Анна', 'Алиса', 'Ольга', 'Виктория',
         'София', 'Юлия', 'Варвара', 'Ксения', 'Елена', 'Мария',
         'Даша', 'Настя', 'Полина'}
is_24 = {'Анна', 'Карина', 'Алиса', 'Любовь', 'Ольга', 'Юлия', 'София',
         'Виктория', 'Ксения', 'Елена', 'Александра', 'Наталья',
         'Надежда', 'Ирина'}
is_25 = {'Анна', 'Алина', 'Алиса', 'Ангелина', 'Ольга', 'София', 'Юлия',
         'Екатерина', 'Виктория', 'Ксения', 'Елена', 'Александра',
         'Наталья', 'Мария', 'Полина'}

names = input("Введите несколько имён девочек через пробел:\n").split()
print("")

for name in names:
    if name in is_21&is_22&is_23&is_24&is_25:
        print(f"Имя {name} есть во всех группах второго курса.")
    elif name in is_21|is_22|is_23|is_24|is_25:
        print(f"Имя {name} встречается не во всех группах второго курса.")
    else:
        print(f"Имени {name} нет в группах второго курса.")
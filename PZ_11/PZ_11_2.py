# Из предложенного текстового файла (text18-17.txt) вывести на экран его содержимое,
# количество знаков препинания. Сформировать новый файл, в который поместить текст в
# стихотворной форме предварительно поставив последнюю строку между первой и второй.

f1 = open("text18-17.txt", encoding="UTF-16")
prep = 0
print(f1.read(), end="\n\n")
f1 = open("text18-17.txt", encoding="UTF-16")
lines = []
for line in f1:
    lines.append(line)
    for char in line:
        if char in {'—',':','.','!','?',',',';','...'}:
            prep += 1
print(f"Знаков препинания: {prep}")

with open("text18-17_2", "w", encoding="UTF-16") as f2:
    pass
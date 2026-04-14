from numpy.ma.core import append

file_1 = "data.txt"
with open(file_1, 'r', encoding='utf-8') as file:
    text = file.read()
print(text)

with open(file_1, 'r', encoding='utf-8') as file:
    text_line = file.readline()
print(text_line)

with open(file_1, 'r', encoding='utf-8') as file:
    text_2 = file.read(10)
print(text_2)

with open(file_1, 'r', encoding='utf-8') as file:
    text_lines = file.readlines()
print(text_lines)

for lines in text_lines:
    print(f"Строка: {lines}")

with open(file_1, 'r', encoding='utf-8') as file:
    text_sym = file.read(6)
    file.seek(0)
    text_sym_2 = file.read(6)
    print(text_sym)
    print(text_sym_2)

with open(file_1, 'r', encoding='utf-8') as file:
    size = file.seek(0, 2)
print(f"Размер файла: {size} байт")

with open(file_1, 'r', encoding='utf-8') as file:
    text = file.read()
print(text)

file_2 = "data.txt"
try :
    f = open(file_2, 'r', encoding='utf-8')
    try :
        text = f.read()
        print(text)
    finally:
        file.close()
except FileNotFoundError:
    print("Ошибка: Файл не найден")

file_1 = "data.txt"
try:
    f = open(file_1, 'r', encoding='utf-8')
    try:
        text = f.read()
        print(text)
    finally:
        file.close()
except FileNotFoundError:
    print("File not found")

try:
    with open(file_1, 'r', encoding='utf-8') as file:
        text = file.readlines()
except FileNotFoundError:
    print("File not found")

file_numbers = "numbers.txt"
try:
    with open(file_numbers, 'r', encoding='utf-8') as file:
        numbers = file.read()
        numbers = numbers.split("\n")
        print(sum(map(int, numbers)))
except FileNotFoundError:
    print("File not found")
finally:
    file.close()

import datetime
file_log = "log.txt"
with open(file_log, 'a', encoding='utf-8') as file:
    file_log = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    file.write(f"{file_log} Запуск программы\n")
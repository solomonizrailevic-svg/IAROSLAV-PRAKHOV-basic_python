set_1 = {2, 3, 4, 5, "tre"}
set_1.add(6)
print(set_1)

set_2 = {"Moscow", "Kazan", "Tehran", "Karachi"}
print(set_2)
# все города уникальные потому что нет повторяющихся элементов

set_3 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
if {5} in set_3:
    set_3.discard(5)
if {15} in set_3:
    set_3.discard(15)

c = "abrakadabra"
set_c = set(c)
print(set_c)
print(len(set_c))

set_4 = set()
set_4.add(10)
set_4.add("Hello")
tuple_c = (1, 2, 3)
set_4.add(tuple_c)
set_4.add([4, 5, 6])
print(set_4)
# не получается добавить список потому что он является изменияемым типом данных

set_5 = {1, 2, 3, 4, 5}
set_6 = {4, 5, 6, 7, 8}
res = set_5 & set_6
res_2 = set_5 | set_6
res_3 = set_5 - set_6
res_4 = set_6 - set_5
res_5 = set_5 ^ set_6
print(res)
print(res_2)
print(res_3)
print(res_4)
print(res_5)

even_numbers = {2, 4, 6, 8, 10}
odd_numbers = {1, 3, 5, 7, 9}
result = even_numbers | odd_numbers
result_2 = even_numbers & odd_numbers
print(result) # обьединяться все элементы и не будет ничего убрано потому что нет дублирующихся элементов
print(result_2) # пересечения не будет поэтому получится пустое множество

text1 = set("программирование")
text2 = set("автоматизация")
text1 & text2
result = text1 - text2
result_2 = text1 ^ text2
print(text1)
print(result)
print(result_2)

set_1 = {i ** 2 for i in range(1, 10) if i % 2 == 0}
print(set_1)

words = ["apple", "banana", "cherry", "apple", "banana", "date", "cherry"]
set_words = {word.upper() for word in words}
print(set_words)

grades = {"Alice": 85, "Bob": 78, "Charlie": 92, "David": 60, "Eve": 88}
new_grade = {}
for key, value in grades.items():
    if value >= 80:
        new_grade[key] = "Отлично"
    else:
        new_grade[key] = "Удовлетворительно"
print(new_grade)

text = {"Python", "automation", "programming", "testing"}
dict_text = {word: len(word) for word in text}
print(dict_text)

digit = int(input("Введите число: "))

first = {
digit:{digit ** 2 for digit in range(1, digit+1)}
    for digit in range(1, digit+1)
}
print(first)

n = int(input("Введите число: "))

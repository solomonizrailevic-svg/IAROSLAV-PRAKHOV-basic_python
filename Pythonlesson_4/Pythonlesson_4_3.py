# Форматирование строк
name = "Yaroslav"
age = "24"

text = f"Мое имя:{name}, Мой возраст:{age}"
# print(text)

# можно сделать и по другому через формат
# text2 = "Мое имя:{0}, Мой возраст:{1}".format(name, age)
# print(text2)

# можно сделать и по другому
text3 = "Мое имя:{imya}, Мой возраст:{vozrast}".format(imya=name,vozrast=age)
print(text3)

# но лучще всего использовать первый вариант с ф-строкой

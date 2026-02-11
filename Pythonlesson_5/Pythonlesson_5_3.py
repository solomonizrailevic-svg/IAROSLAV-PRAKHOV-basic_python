# методы списка
a = [415, 33, 22, 234, 6667, 454]
print(a)
a.append(200)
a.append("fff")
a.append(True)
a.append([True, False])
print(a)
a.insert(1,55)
print(a) # можно добавлять разные элементы, как булевые, так и строки и тд
a.append(True)
#удалить элемент
a.remove(True) # Удаляется только первый найденный элемент(в данном случае первый добавленный тру)
print(a)

# # Удаление элемента по индексу
# last_el = a.pop()
# print(a)
# print(last_el)

index_el = a.pop(3)
print(a)
print(index_el)

# #полное очищение списка
# a.clear()
# print(a)

# копирование списка
b = a[:]
b = list(a)
b = a.copy()
print(id(a))
print(id(b))

print(a)
print(a.count(True))
print(a.count([True, False]))

# нахождение элемента по индексу
print(a)
print(a.index([True, False]))
print(b.index([True, False]))
print(a.index([True, False], 5))

print(a.reverse()) # если писать так то он поменяет данные в памяти пайтона но ничего не выведет на экран, поэтому
a.reverse()
print(a)

# сортировка
c = [22, 33434, 546364, 47467575, 24523414.222, 23231]
c.sort()
print(c)
c.sort(reverse=True)
print(c) # sort меняет текущий список, sorted возвращает текущий список
d = sorted(c)
print(d)
# d.sorted не получится вывести как получается выводить d.sort, d.sorted только для работы с переменной

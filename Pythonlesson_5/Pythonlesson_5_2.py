streets = ["Tukaya", "Pushkina", "Karbysheva", "Tatarstan", "Khusayina Mavlyutova"]
ages = [24, 34, 22]
# print(streets[2:4])
# print(streets[2:])
# streets_2 = streets
# streets_3 = streets[::]
# print(id(streets))
# print(id(streets_2))
# print(id(streets_3))
# print(streets_2)
#
# streets_2 = list(streets)
# print(id(streets))
# print(id(streets_3))
# # присваивание списка не дает копию
# streets_3 = streets
# streets[0] = "Chernyshevskogo"
# print(streets)
# print(streets_3)
# print(id(streets))
# print(id(streets_3))
# # поменяется и 0 индекс и в стритс и в стритс 3 потому что оба ссылаются на один элемент памяти

# print(streets)
# print(streets[::2])
# print(streets[1::2])
# print(streets[1:3:2])
# print(streets[::-1])
# print(streets[::-1])
# print(streets[-3::-1])

# print(streets)
# print(streets[::-1])
# print(streets[::-2])

# # замена на другие элементы
print(streets)
streets[2:4] = [34, 65]
streets[2:4] = 34, 65
print(streets)
print(streets)

# # сравнение двух списков между собой
# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)

a = [1, 2, "4"]
b = [1, 2, 3]
# print(a >= b) # нельзя будет так сравнить, потому что есть элементы строки "4", поэтому можно будет сравнить только след образом
print(a == b)
print(a != b) # то есть только равно\неравно
cities = ["Kazan", "Chelny", "Elabuga", "Almetyevsk", "Laishevo"]
cities2 = cities
# print(cities2 == cities)
# print(cities2)
#
# print(cities[2], cities[3])
# print(cities[3:])
# print(cities[:3])
# print(cities[:])
# print(cities[:-3:-1])
#
# print(cities[::2])
# print(cities[::-1])
# print(cities[::-2])

cities[2:4] = "Сочи", "Нижний Новгород"
print(cities)
cities[1::2] = ["Город"] * len(cities[1::2])
print(cities)
cities[1:3] = "Волгоград", "Омск"
print(cities)

u = [1, 2, 3]
v = [4, 5, 6]
print(u + v)
b = ["Python", "rocks"]
print(b * 2)

j = [1, 2, 3]
jj = [1, 2, 3]
print(j == jj) # списки равны
print([10, 5, 3] > [5, 10, 3])
# print([1, 2, 3] и [1, 2, "abc"]) # Выдает ошибку, потому что во втором списке есть буквенное значение

chars = list("Python")
print(max(chars))
print(min(chars))
print(sum(chars)) # сложение не удалось по причине того, что нельзя суммировать элементы str






cities = ["Москва", "Тверь", "Вологда"]
numbers = [1, 2, 3, 4, 5]
mixed = [22, "Иван", True, 22.3 ]
print(cities[0])
print(numbers[-1])
# print(cities[10]) # выдает ошибку потому что в списке нет элемента под индексом 10

numbers[1] = 10
print(numbers)

mixed[-1] = "Python"
print(mixed)

print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(sorted(numbers))

o = [1, 2, 3]
l = [4, 5]
print(o + l)
k = ["Python", "is", "awesome"]
print(k + k + k)

print([3] in numbers)
print(["Москва"] in cities)
print([1, 2] in mixed)
del numbers[3]
print(numbers)
del cities[-1]
print(cities)
v = "Python"
print(list("".join(v)))
print(max(v))
print(min(v))
print(sum(v)) # выдало ошибку, потому что операции сложения можно проводить с числами


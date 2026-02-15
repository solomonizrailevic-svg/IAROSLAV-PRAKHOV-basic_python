numbers = [5, 10, 15]
numbers.append(20)
print(numbers)
numbers.insert(1, 7)
print(numbers)
numbers.append("Python")
print(numbers)

numbers.remove(20)
print(numbers)
pl = numbers.pop(-1)
print(numbers)
print(pl)

numbers.remove(10)
print(numbers)
pk = numbers.pop(-1)
print(numbers)
print(pk)
numbers.pop(1)
print(numbers)
numbers.clear()
print(numbers)

letters = ["a", "b", "c"]
b = letters.copy()
b = list(letters)
print(b == letters)

marks = [2, 3, 5, 3, 4, 5, 2, 3]
print(marks.count(3))
print(marks.index(5))
print(6 in marks)
# print(marks.index(6))

nums = [8, 2, 5, 1, 7]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)
nums.reverse()
print(nums)

cities = ["London", "Paris", "New York"]
cities.sort()
print(cities)
g = sorted(cities)
print(g)

chars = list("programming")
print(chars.count("g"))
chars.reverse()
print(chars)
chars.sort()
print(chars) # произошла сортировка по возрастанию числового кода каждого символа


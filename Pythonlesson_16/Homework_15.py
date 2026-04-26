data = ["Python", 123, "Java", 456, "C++", 789]
gen = (item for item in data if isinstance(item, str))
print(" ".join(gen))

import random
gen_2 = (random.randint(0, 100) for x in range(10))
print(max(list(gen_2)))


with open("words.txt", 'r', encoding='utf-8') as file:
    g = (word for line in file for word in line.split() if len(word) > 5)
    ge = (line for line in file if "Python" in line)
    print(" ".join(g))
    print(" ".join(ge))

def gen():
    while True:
        yield random.randint(0, 100)

for x in gen():
    print(x, end=" ")
    if x == 50:
        break

n = int(input())
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(is_prime(n))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_generator(N):
    count = 0
    num = 2
    while count < N:
        if is_prime(num):
            yield num
            count += 1
        num += 1
print(*prime_generator(5))

def gen_api():
    n = 1
    while True:
        yield f"Получены данные {n}"
        n += 1
g = gen_api()
for _ in range(5):
    print(next(g))

top = input().split()
nums = list(map(int, top))
squares = map(lambda x: x**2, nums)
print(list(squares))

text_1 = ["Москва", "Санкт-Петербург", "Казань"]
text_1_map = map(lambda str_1: str_1.upper(), text_1)
print(list(text_1_map))

numbers = [15, 30, 45, 22, 60, 77, 90, 100]
numb_two_three = filter(lambda num: num % 3 == 0 and num % 5 == 0, numbers)
print(list(numb_two_three))

list_11 = ["hello", "world42", "python3", "abc", "123", "data1science"]
# list_11_s = filter(lambda x: x if x.isinstance(int) else None, list_11)
list_11_s = filter(lambda x:any(x.isdigit() for x in x), list_11)
print(list(list_11_s))

countries = ["Россия", "Франция", "Германия"]
capitals = ["Москва", "Париж", "Берлин"]
z = dict(zip(countries, capitals))
print(z)

data = [(1, 'a'), (2, 'b'), (3, 'c')]
z = list(zip(data))
print(z)
z1 = zip(*z)
print(list(z1))

names = ["петр", "Иван", "мария", "Анна"]
result = sorted(names, key=lambda x: x[0].islower())
print(result)

products = [("Телефон", 500), ("Ноутбук", 1000), ("Планшет", 700)]
result = sorted(products, key=lambda x: x[1])
print(result)
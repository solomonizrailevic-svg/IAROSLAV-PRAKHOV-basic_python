# items = [5, "hello", [1, 2], 3.14, {"a": 1}, "world"]
# fltr = filter(lambda x: isinstance(x, str | list), items)
# print(list(fltr))
#
# def describe_type(x):
#     if isinstance(x, bool):
#         print("Это булевое значение")
#     elif isinstance(x, str):
#         print("Это строка")
#     elif isinstance(x, int | float):
#         print("Это число")
#     else:
#         print("Неизвестный тип")
#     return x
# describe_type(5)
# describe_type(True)
# describe_type("Привет")
# describe_type([1, 2, 3])
from fontTools.merge.util import avg_int
from pyparsing import str_type

#
# def filter_list(f, data: list[int]) -> list[int]:
#     result = []
#     for x in data:
#         if f(x):
#             result.append(x)
#     return result
#
# print(filter_list(lambda x: x > 3, [1, 3, 5, 7]))

# def print_info(name:str, age:int, tags:list) -> None:
#     print(name, age, tags)
#
# print_info("Иван", 24, ["python", "dev"])
#
# def analyze(data: list[int]):
#     if not data:
#         print("Список пуст")
#         return
#
#     count = len(data)
#     avg = sum(data) / count
#
#     print("Количество:", count)
#     print("Среднее:", avg)
#
# print(analyze([2, 3, 4]))

# flags = [True, True, True, False]
# print(all(flags) == True)
# print(any(flags) == True)

# field = ['x', 'x', 'x', 'o', 'o', '', '', '', '']
# print(field[0] == field[1] == field[2] == 'x')

P = ['0', '0', '0', '*', '0']
print(any(x == "*" for x in P))

import random

colors = ["red", "green", "blue", "yellow", "purple"]
colors_random = random.choice(colors)
print(f"Выбран цвет: {colors_random}")

random.seed(123)
x = random.uniform(0, 100)
y = random.uniform(0, 100)
z = random.uniform(0, 100)
w = random.uniform(0, 100)
e = random.uniform(0, 100)
t = random.uniform(0, 100)
r = random.uniform(0, 100)
q = random.uniform(0, 100)
s = random.uniform(0, 100)
c = random.uniform(0, 100)
print(f"{x}, {y}, {z}, {w}, {e}, {t}, {r}, {q}, {s}, {c}")

def greet(name:str) -> str:
    return f"Привет, {name}"
print(greet("Ярослав"))

def multiply(a: int, b: float) -> int | float:
    return a * b
print(multiply(5, 4))
print(multiply.__annotations__)

def area(length: float, width: float) -> float:
    return length * width
print(area.__annotations__)

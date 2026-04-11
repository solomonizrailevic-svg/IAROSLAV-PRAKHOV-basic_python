# from math import sqrt, pow
# print(sqrt(64))
# print(pow(5, 3))
#
# import random
# num = random.randint(1,10)
# languages = ["Python", "Java", "C++"]
# lang_choice = random.choice(languages)
# print(f"Случайное число: {num}")
# print(f"Случайный язык: {lang_choice}")
#
# import my_module
# print(my_module.add(3, 5))
# print(my_module.multiply(4, 6))

# import time
#
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"Код выполнялся:{end - start}")
#         return result
#     return wrapper
# @decorator
# def timer_func():
#     time.sleep(2)
# timer_func()

# import requests
#
# response = requests.get("https://api.github.com")
# print(response.status_code)

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 50]

plt.plot(x, y, marker='o')
plt.title("Пример графика")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
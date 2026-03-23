from codecs import ignore_errors


def greet(name):
    print(f"Привет{name}! Добро пожаловать!")
greet(" Анна")

def square(num):
    return num ** 2
num = 5
print(square(num))

def is_even(num):
    return num % 2 == 0
print(is_even(6))

def repeat_string(text, times):
    return text * times
print(repeat_string("hello", 4))

def add(a, b):
    return a + b
print(add(2, 3))

def get_max(a, b, c):
    return max(a, b, c)
print(get_max(2, 3,10))

def calculate(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b
print(calculate(2, 3, "+"))

def reverse_string(text):
    return text[::-1]
print(reverse_string("hello"))


def compare_strings(s1, s2, ignore_case=True, ignore_spaces=True):
    if ignore_spaces:
        s1 = s1.strip()
        s2 = s2.strip()
    if ignore_case:
        s1 = s1.lower()
        s2 = s2.lower()
    return s1 == s2
print(compare_strings("hello", "Hello ", False, True))

def summarize(*args):
    total = 0
    for item in args:
        if isinstance(item, (int, float)):
            total += item
    return total
print(summarize(1, 2, "abs"))

def create_profile(name, age, **extra):
    return {"name": name, "age": age, "extra": extra}
print(create_profile(name="Iaroslav", age=25, job="Engineer"))


def process_orders(*orders, discount=0):
    total = sum(orders)
    final = total * (100 - discount) // 100 if discount else total

    print(f"Сумма заказа: {total}")
    print(f"С учетом скидки: {final}")

    return final
print(process_orders(150, 240, 340, discount=2))

def merge_lists(*lists):
    result = []
    for lst in lists:
        result.extend(lst)          # или result += lst
    return result
print(merge_lists([22, 33], [23, 456], [56, 73]))

def merge_dicts(*dicts):
    result = {}
    for d in dicts:
        for key, value in d.items():
            result[key] = value
    return result
print(merge_dicts({"a": 1, "b": 2, "c": 3}))
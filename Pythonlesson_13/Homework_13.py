def my_decorator(func):
    def wrapper():
        func()
    return wrapper

@my_decorator
def say_hello():
    text = "Hello, World!"
    print(text.upper())
# say_hello()

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
               res = func(*args, **kwargs)
            return res
        return wrapper
    return decorator

@repeat(3)
def hello():
    print("hello world")
hello()


import time

def execution_time(repeat=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            times = []
            for _ in range(repeat):
                start = time.time()
                res = func(*args, **kwargs)
                end = time.time()
                times.append(end - start)
            avg_time = sum(times) / len(times)
            print(f"Функция {func.__name__} была выполнена {repeat} раз")
            print(f"Среднее время: {avg_time}")
            return res
        return wrapper
    return decorator

@execution_time(3)
def slow_function():
    time.sleep(5)
    print("Spasibo")
    return "Готово"

slow_function()

def cache(func):
    cache_storage = {}
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key in cache_storage:
            print(f"Беру из кэша{args}")
            return cache_storage[key]
        print(f"Вычисляю для аргументов{args}")
        result = func(*args, **kwargs)
        cache_storage[key] = result
        return result
    return wrapper
@cache
def slow_square(n):
    return n * n

@cache
def add(a, b):
    return a + b

print(slow_square(4))
print(slow_square(4))
print(slow_square(5))
print(slow_square(5))

print(add(2, 3))
print(add(2, 3))
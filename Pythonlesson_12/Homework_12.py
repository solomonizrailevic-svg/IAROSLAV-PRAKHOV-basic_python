square = lambda a: a**2
def square(a):
    return a**2
print(square(4))

number = lambda a: a%2
def number(a):
    if a % 2 == 0:
        print(f"{a} - четное число")
    else:
        print(f"{a} - нечетное число")
        return number
print(number(3))

def sort_by_last_letter(words):
    return sorted(words, key=lambda word: word[-1])
print(sort_by_last_letter(["Yok", "Hayir", "Evet","Hala"]))

def multiply_by(n, x):
    def multiply_func():
        return x * n
    return multiply_func

multiply_six = multiply_by(5, 5)

multiply_six()

print(multiply_six())


def counter(start=0):
    count = start
    def counter_func():
        nonlocal count
        count += 1
        return count
    return counter_func

c1 = counter(5)
c2 = counter()

print(c1())
print(c1())
print(c2())
print(c2())
print(c1())
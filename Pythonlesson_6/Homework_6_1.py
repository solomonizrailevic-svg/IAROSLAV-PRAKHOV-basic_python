x =int(input("Введите число: "))
if x > 0:
    print("Число положительное")
if x < 0:
    print("Число отрицательное")
elif x == 0:
    print("Число равно нулю")

x =int(input("Введи число: "))
if x % 2 == 0:
    print("Число четное")
if x % 3 == 0:
    print("Число нечетное")

x =int(input("Введи число: "))
chisla =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if x in chisla:
    print("Число в диапазоне")
else:
    print("Число вне диапазона")
from selectors import SelectSelector

a = int(input("Введи число: "))
b = int(input("Введи число: "))
if a < b:
    a, b = b, a
print(a, b)
if a >= b:
    print("По убыванию:", a, b)
else:
    print("По убыванию:", b, a)


a = int(input("Введи число: "))
b = int(input("Введи число: "))
if a < b:
    print(a)
if a > b:
    print(b)

marks = [3, 4, 5, 2, 5, 4]
if [2] in marks:
    print("Есть неудовлетворительная оценка")
else:
    print("Все оценки положительные")

x =(int(input("Введи число: ")))
if (x % 3 == 0) and (x % 5 == 0):
    print("Число делится на 3 и на 5")
elif x % 3 == 0:
    print("Число делится только на 3")
elif x % 5 == 0:
    print("Число делится только на 5")
elif (x % 3 != 0) and (x % 5 != 0):
    print("Число не делится на 3 и 5")

password = (input("Введите свой пароль: "))
if password == "admin123":
    print("Доступ разрешен")
else:
    print("Доступ запрещен")

amount = (int(input("Введите сумму покупки")))
if amount > 5000:
    g = amount / 100 * 10
    print(g)
if amount < 5000:
    g = amount / 100 * 5
    print(g)
else:
    print("Без скидки")

year = (int(input("Введите год: ")))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            print("Год високосный")
else:
    print("Год не високосный")
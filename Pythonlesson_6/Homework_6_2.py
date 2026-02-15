x = (int(input("Введите число от 1 до 5: ")))
if x == 5:
    print("Отлично")
elif x == 4:
    print("Хорошо")
elif x == 3:
    print("Удовлетворительно")
elif x == 2 or x == 1:
    print("Неудовлетворительно")
elif x > 5 or x < 1:
    print("Некорректная оценка")
from selectors import SelectSelector

c = (int(input("Назовите который сейчас час: ")))
if c >= 6 and c <= 11:
    print("Утро")
elif c >= 12 and c <= 17:
    print("День")
elif c >= 18 and c <= 21:
    print("Вечер")
elif c <= 5 or c >= 21 and c <= 24:
    print("Ночь")
elif c != (0 - 24):
    print("Введено некорректное время")

tem = int(input("Введите температуру: "))
if tem <= -10:
    print("Очень холодно")
elif tem >= -10 and tem <= 0:
    print("Холодно")
elif tem >= 1 and tem <= 10:
    print("Прохладно")
elif tem >= 11 and tem <= 25:
    print("Тепло")
elif tem > 25:
    print("Жарко")

visokos = int(input("Введите високосный год: "))
if visokos % 4 == 0 and visokos % 100 != 0 or visokos % 400 == 0:
    print("Введен високосный год")
else:
    print("Введен не високосный год")

op = int(input("Введите число: "))
era = int(input("Введите второе число: "))
tsia = input("Выберите какую операцию провести с этими числами(+, -, *, /): ")
if tsia == "+":
    print(op + era)
elif tsia == "-":
    print(op - era)
elif tsia == "*":
    print(op * era)
elif tsia == "/" and era != 0:
    print(op / era)
elif era == 0:
    print("Ошибка!Деление на ноль")
else:
    print("Некорректная операция")
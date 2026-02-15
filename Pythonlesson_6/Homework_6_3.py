x = int(input("Введите число: "))
ty ="Четное число" if x % 2 == 0 else "Нечетное число"
print(ty)

c =int(input("Введите число: "))
v =int(input("Введите второе число: "))
xl = c if c > v else v
print(xl)

c1 =int(input("Введите число: "))
plzh = "Число положительное" if c1 > 0 else "Число отрицательное" if c1 < 0 else "Число равно нулю"
print(plzh)

vzrst = int(input("Введите свой возраст: "))
vxod = "Вход разрешен" if vzrst >= 18 else "Вход запрещен"
print(vxod)

pk = int(input("Введите сумму покупки: "))
pkpka = (pk / 100 * 10) if pk > 5000 else "Скидки нет"
print(pkpka)
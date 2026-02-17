n = int(input("Введите число: "))
i = 0
while i <= n:
    print(i)
    i += 1

n = int(input("Введите число: "))
i = 0
sum = 0
while i <= n:
    if i % 2 == 0:
        sum += i
    i += 1
print(sum)

n = int(input("Введите натуральное число: "))
if n == 0:
    print("В числе 0 1 цифра")
else:
    count = 0
    while n > 0:
        n = n // 10  # убираем последнюю цифру
        count += 1

    print("Количество цифр:", count)

n = int(input("Введите натуральное число: "))
count = 0
while n > 0:
    n = n // 10
    count = n
    if n >= count:
        count = n
        print("Наибольшая цифра: ", count)

n = int(input("Введите натуральное число: "))
if n == 0:
    print("Максимальная цифра: 0")
else:
    mx = 0
    while n > 0:
        max1 = n % 10
        if max1 > mx:
            mx = max1
        n //= 10
    print("Максимальная цифра:", mx)

n = input("Введите правильный пароль: ")
password = "qwerty123"
while True:
    if n == password:
        print("Доступ разрешен")
        break
    else:
        print("Введен неверный пароль")
        n = input("Введите правильный пароль: ")

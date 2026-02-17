список = [7, 3, 10, 1, 5]
i = 0
while i < len(список):
    if список[i] % 2 == 0:
        print(список[i])
        break
    i += 1
else:
    print("Четное число не найдено")

число = 1
sum1 = 0
while число != 0:
    число = int(input("Введите ноль: "))
    if число > 0:
        sum1 += число
    if число < 0:
        continue
print(sum1)

a = int(input("Введите число: "))
b = int(input("Введите второе число: "))
i = a
while i <= b:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1

n = int(input("Введите число: "))
if n < 2:
    print(n, "— не простое число")
else:
    i = 2
    while i < n:
        if n % i == 0:
            print("Не простое — делится на", i)
            break
        i += 1
    else:
        print(n, "— простое число")


ввод = int(input("Введите число: "))
p = ввод
while ввод > 0:
    if ввод == 0:
        break
    if ввод > p:
        p = ввод
    ввод = int(input("Введите число: "))
print(p)


lst = [7, 3, 10, 1, 5]
i = 0
while i < len(lst):
    if lst[i] % 2 == 0:
        print(lst[i])
        break
    i += 1
else:
    print("Четное число не найдено")

numb = 1
sum1 = 0
while numb != 0:
    numb = int(input("Введите ноль: "))
    if numb > 0:
        sum1 += numb
    if numb < 0:
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


access = int(input("Введите число: "))
p = access
while access > 0:
    if access == 0:
        break
    if access > p:
        p = access
    access = int(input("Введите число: "))
print(p)


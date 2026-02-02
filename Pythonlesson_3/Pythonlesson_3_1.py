# a = "string"
# print(34, a)
# print(34, 432, "qwerty", a)

# a = 12
# b = 34.54
# c = 89
# print(a, b, c)
# print(a, b, c, sep=" | ", end="\n")
# print(a, b, c, sep=" | ")
#
# print(a, b, c, sep=" | ", end=" ")
# print(a, b, c, sep=" | ")
# #
# print("Результат умножения числа", a,"и числа", b, " равен", a * b)
# #либо
# print(f"Результат умножения числа {a} и числа {b} равен {a * b}") #f-string

a = float(input())
print(type(a))
print(a)

a = float(input("Введите длину прямоугольника: ",))
b = float(input("Введите ширину прямоугольника: ",))
print(f"Периметр:{2 * (a + b)}")
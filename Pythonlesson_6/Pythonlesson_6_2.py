# # Вложенные условияс когда одно условие есть внутри другого (0 - 9 - цифры, 92 и больше - числа)
# x = int(input("Введите число: "))
# #
# if x % 2 == 0:
#     if 0 <= x <= 9:
#         print("x - четная цифра")
#     else:
#         print("x - четное число")
# else:
#     if 0 <= x <= 9:
#         print("x - нечетная цифра")
#     else:
#         print("x - нечетное число")

"""
1 - Kupit mebel
2 - Kupit mashinu
3 - Kupit dom
4 - Kupit kvartiru
"""
item = int(input("Выбрать объект(1-4): "))
# if item == 1:
#     print("Выбран пункт: Kupit mebel")
# else:
#     if item == 2:
#         print("Выбран пункт: Kupit mashinu")
#     else:
#         if item == 3:
#             print("Выбран пункт: Kupit dom")
#         else:
#             if item == 4:
#                 print("Выбран пункт: Kupit kvartiru") # это неудобно, поэтому есть оператор элиф

if item == 1:
    print("Выбран пункт: Kupit mebel")
elif item == 2:
    print("Выбран пункт: Kupit mashinu")
elif item == 3:
    print("Выбран пункт: Kupit dom")
elif item == 4:
    print("Выбран пункт: Kupit kvartiru")
else:
    print("error, choose from 1 to 4")
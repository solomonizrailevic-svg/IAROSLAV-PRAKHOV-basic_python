# индексы строк!!! важно
s = "Privet, Yaroslav"

"""
0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15        
P  r  i  v  e  t  ,     Y  a  r  o  s  l  a  v
                        -8 -7 -6 -5 -4 -3 -2 -1
"""
# print(s[6])
# print(s[11])
# print(s[17])
# print(s[len(s) - 1])

# # отрицательный индекс
# print(s[-12])

# print("Строка"[3])

#срезы строк
# print(s[8:13])
# print(s[8:])
# print(s[:6])
# print(s[:])
# s2 = s[:]
# print(s2)
# print(id(s))
# print(id(s2))
# s2 *= 2
# print(s2)
# print(id(s))
# print(id(s2))

# print(s[5:-4])
# print(s[-5:2])
# print(s[-6:11])
# # использование шага!!! важно для собеседований
# print(s[1:10:2])
# print(s[::2])
# print(s[::3])
# print(s[::-2])
# print(s[::-1])

# #исправление элементов в переменной
# print(s[:8] + "y" + s[9:])

s2 = """
Jeffrey Epstein
"""
print((s2[1:8] + " Epstein") == s2[1:16])
print(type(s2))
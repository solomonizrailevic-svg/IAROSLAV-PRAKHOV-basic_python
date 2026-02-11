streets = ["Tukaya", "Pushkina", "Karbysheva"]

"""
        0           1           2
  ["Tukaya"]  ["Pushkina"] ["Karbysheva"]
        -3         -2         -1
"""
ages = [24, 34, 22]
# print(streets[-2])
# print(ages[-1])
# # print(ages[3]) # выдаст ошибку потому что 3 нет
#
# #вычисления среднего возраста
# avg_age = sum(ages) / len(ages)
# avg_age2 = int(sum(ages) / len(ages))
# print(avg_age)
# print(avg_age2)
#
# # списки это изменяемый тип данных
# ages[1] = 31 # 1 это индекс в списке
# print(ages)

# # lst = ["Волгоград", 223, 32, 343, True, False, [22 +3]] # в списке может быть все что угодно
# lst = [] # первый варик как создать список
# lst2 = list() #второй варик как создать список
# lst3 = list("Volgograd ")
# print(lst3)

# print(len(lst3))
# print(max(lst3))
# print(max(ages))
# print(min(ages))
# print(min(lst3))
# print(sum(ages))
# print(sorted(ages)) # сортируется по нарастанию
# print(sorted(lst3))
# print(sorted(lst3, reverse=True)) # переворачивает содержимое переменной
# print(sorted(ages, reverse=True))

# print(sum(lst3)) # суммировать можно только инт , но не строки
print(streets + ages)
result = streets + ages
# print(result + "A") # нельзя, нужно чтобы было сложние списка со списком, то есть
print(result + ["A"])
print(result + [2.4])
print("Karbysheva" in result)
# однако можно искать только цельную строку в списке чтобы было тру
print("bysheva" in result) # будет фолс потому что не находит части слова, может только цельную строку найти
# изменение текущего списка в пайтоне
result.append("1212")
print(result)
result.append("1212")
result.append([2, 5])
print([2, 5] in result)
# удаление индекса элемента
del result[-1]
print(result)
del result[1]
print(result)
del result[1]
print(result)
